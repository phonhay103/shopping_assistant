import wx
import noname
import psycopg2
import numpy as np
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

host='localhost'
database="CSDLv3"
user="postgres"
password="Your_password"
port="5433"

class main_frame(noname.MainFrame):
   def __init__(self, parent):
      noname.MainFrame.__init__(self, parent)

   def random_item(self, event):
      with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
         cur = conn.cursor()
         cur.execute("SELECT COUNT(*) FROM items;")
         N = cur.fetchone()[0]
         random_idx = np.random.randint(1, N+1)

         cur.execute("SELECT p.item_id FROM (SELECT ROW_NUMBER() OVER(), item_id FROM items) p WHERE row_number = %s;", (random_idx,))
         item_id = cur.fetchone()[0]
         cur.close()
      show_item(item_id)
      return super().random_item(event)
   
   def random_shop(self, event):
      with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
         cur = conn.cursor()
         cur.execute("SELECT cal_total_shops();")
         N = cur.fetchone()[0]
         random_idx = np.random.randint(1, N+1)

         cur.execute("SELECT p.shop_id FROM (SELECT ROW_NUMBER() OVER(), shop_id FROM shops) p WHERE row_number = %s;", (random_idx,))
         shop_id = cur.fetchone()[0]
         cur.close()
      show_shop(shop_id)
      return super().random_shop(event)

   def show_all_items(self, event):
      show_100_lowest()
      return super().show_all_items(event)

   def show_all_items2(self, event):
      show_100_highest()
      return super().show_all_items2(event)

   def show_item_when_click(self, event):
      idx = frame.m_listCtrl1.GetFocusedItem()
      if idx != -1:
         id = frame.m_listCtrl1.GetItemText(idx)
         if frame.m_listCtrl1.GetColumn(0).GetText() == 'Item_ID':
            show_item(id)
         else:
            show_shop(id)
      return super().show_item_when_click(event)

   def show_shops_by_rating(self, event):
      show_all_shops_by_rating()
      return super().show_shops_by_rating(event)

   def top_100_fav_HN(self, event):
      show_100_fav_HN()
      return super().top_100_fav_HN(event)

   def SRM(self, event):
      show_SRM()
      return super().SRM(event)

   def item_search(self, event):
      show_item_search()
      return super().item_search(event)

   def button8(self, event):
      self.m_listCtrl1.DeleteAllItems()
      self.m_listCtrl1.DeleteAllColumns()

      self.m_listCtrl1.InsertColumn(0, 'Item_ID')
      self.m_listCtrl1.InsertColumn(1, 'Item_Name')
      self.m_listCtrl1.InsertColumn(2, 'Shop_ID')
      self.m_listCtrl1.InsertColumn(3, 'Shop_name')
      self.m_listCtrl1.InsertColumn(4, 'Category')
      self.m_listCtrl1.InsertColumn(5, 'City')
      self.m_listCtrl1.InsertColumn(6, 'Price')
      self.m_listCtrl1.InsertColumn(7, 'Brand')
      self.m_listCtrl1.InsertColumn(8, 'Rating')

      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()
         # item_id, item_name, shop_id, shop_name, category_name, city_name, price, brand, rating
         cur.execute("select * from search_item_by_etc('Kem v?? s???a d?????ng da','Tp. H??? Ch?? Minh',50000,500000);")
         a = cur.fetchall()
         for i in range(len(a)):
            self.m_listCtrl1.InsertStringItem(i, a[i][0])
            self.m_listCtrl1.SetStringItem(i, 6, str(a[i][6]))
            self.m_listCtrl1.SetStringItem(i, 7, a[i][7])
            self.m_listCtrl1.SetStringItem(i, 8, str(round(a[i][8], 2)))
            for j in range(1, 6):
               self.m_listCtrl1.SetStringItem(i, j, str(a[i][j]))

            if i % 2 == 0:
               self.m_listCtrl1.SetItemBackgroundColour(i, "grey")
               self.m_listCtrl1.SetItemTextColour(i, 'white')
         cur.close()
      return super().button8(event)

   def Demo(self, event):
      self.m_listCtrl1.DeleteAllItems()
      self.m_listCtrl1.DeleteAllColumns()

      self.m_listCtrl1.InsertColumn(0, 'Item_ID')
      self.m_listCtrl1.InsertColumn(1, 'Name')
      self.m_listCtrl1.InsertColumn(2, 'Price')
      self.m_listCtrl1.InsertColumn(3, 'Brand')
      self.m_listCtrl1.InsertColumn(4, 'Shop')
      self.m_listCtrl1.InsertColumn(5, 'City')
      self.m_listCtrl1.InsertColumn(6, 'Favourite')
      self.m_listCtrl1.InsertColumn(7, 'Sold')
      self.m_listCtrl1.InsertColumn(8, 'Rating')

      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()
         # item_id, item_name, price, brand, shop_name, city_name, num_of_fav, num_of_sold
         cur.execute("""SELECT item_id, item_name, price, brand, shop_name, city, num_of_fav, num_of_sold, avg_rating
                        FROM items NATURAL JOIN shops
                        WHERE item_name LIKE '%m??%'
                        AND price BETWEEN 30000 AND 80000
                        AND city = 'H?? N???i'
                        AND rating >= 3
                        ORDER BY price, rating desc;
                                 """)
         a = cur.fetchall()
         for i in range(len(a)):
            self.m_listCtrl1.InsertStringItem(i, a[i][0])
            self.m_listCtrl1.SetStringItem(i, 1, a[i][1])
            self.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
            self.m_listCtrl1.SetStringItem(i, 8, str(round(a[i][8], 2)))
            
            for j in range(3, 8):
               self.m_listCtrl1.SetStringItem(i, j, str(a[i][j]))

            if i % 2 == 0:
               self.m_listCtrl1.SetItemBackgroundColour(i, "grey")
               self.m_listCtrl1.SetItemTextColour(i, 'white')
         cur.close()      
      return super().Demo(event)

class item_frame(noname.Item):
   def __init__(self, parent, item_id):
      super().__init__(parent)
      self.item_id = item_id
   
   def click_on_shopname(self, event):
      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()
         cur.execute('SELECT shop_id FROM shops WHERE shop_name = %s;', (self.shopname.GetLabel().replace('Shop: ', ''),))
         show_shop(cur.fetchone()[0])
         cur.close()
      return super().click_on_shopname(event)
   
   def brand_click(self, event):
      brand_name = self.brand.GetLabel().replace('Th????ng hi???u: ', '')
      if brand_name == 'No Brand':
         return super().brand_click(event)
      
      frame.m_listCtrl1.DeleteAllItems()
      frame.m_listCtrl1.DeleteAllColumns()

      frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
      frame.m_listCtrl1.InsertColumn(1, 'Name')
      frame.m_listCtrl1.InsertColumn(2, 'Price')
      frame.m_listCtrl1.InsertColumn(3, 'Brand')

      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()
         cur.execute('SELECT item_id, item_name, price FROM items WHERE brand = %s LIMIT 100;', (brand_name,))
         a = cur.fetchall()
         for i in range(len(a)):
            frame.m_listCtrl1.InsertStringItem(i, a[i][0])
            frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
            frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
            frame.m_listCtrl1.SetStringItem(i, 3, brand_name)
            if i % 2 == 0:
               frame.m_listCtrl1.SetItemBackgroundColour(i, "grey")
               frame.m_listCtrl1.SetItemTextColour(i, 'white')
         cur.close()
      self.Destroy()
      return super().brand_click(event)

   def city_click(self, event):
      city_name = self.city.GetLabel().replace('G???i t???: ', '')
      
      frame.m_listCtrl1.DeleteAllItems()
      frame.m_listCtrl1.DeleteAllColumns()
      frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
      frame.m_listCtrl1.InsertColumn(1, 'Name')
      frame.m_listCtrl1.InsertColumn(2, 'Price')
      frame.m_listCtrl1.InsertColumn(3, 'City')

      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()
         cur.execute('''SELECT item_id, item_name, price 
                        FROM items, shops, cities
                        WHERE items.shop_id = shops.shop_id
                        AND shops.city_id = cities.city_id
                        AND city_name = %s
                        LIMIT 100;''', (city_name,))
         a = cur.fetchall()
         for i in range(len(a)):
            frame.m_listCtrl1.InsertStringItem(i, a[i][0])
            frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
            frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
            frame.m_listCtrl1.SetStringItem(i, 3, city_name)
            if i % 2 == 0:
               frame.m_listCtrl1.SetItemBackgroundColour(i, "grey")
               frame.m_listCtrl1.SetItemTextColour(i, 'white')
         cur.close()

      self.Destroy()
      return super().city_click(event)

class CanvasPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)
        self.SetSizer(self.sizer)
        self.Fit()

class shop_frame(noname.Shop):
   def __init__(self, parent, shop_id):
      super().__init__(parent)
      self.shop_id = shop_id

class search_frame(noname.ItemSearch):
   def __init__ (self, parent):
      super().__init__(parent)

   def get_result(self, event):
      self.m_listCtrl2.DeleteAllItems()
      self.m_listCtrl2.DeleteAllColumns()

      self.m_listCtrl2.InsertColumn(0, 'Item_ID')
      self.m_listCtrl2.InsertColumn(1, 'Name')
      self.m_listCtrl2.InsertColumn(2, 'Price')
      self.m_listCtrl2.InsertColumn(3, 'Brand')
      self.m_listCtrl2.InsertColumn(4, 'Shop')
      self.m_listCtrl2.InsertColumn(5, 'City')
      self.m_listCtrl2.InsertColumn(6, 'Favourite')
      self.m_listCtrl2.InsertColumn(7, 'Sold')
      self.m_listCtrl2.InsertColumn(8, 'Rating')

      with psycopg2.connect(host=host,
                           database=database,
                           user=user,
                           password=password,
                           port=port) as conn:
         cur = conn.cursor()

         search_word = self.m_searchCtrl1.GetValue()
         cur.execute(f"""SELECT item_id, item_name, price, brand, shop_name, city, num_of_fav, num_of_sold, avg_rating
                        FROM items NATURAL JOIN shops
                        WHERE item_name LIKE '%{search_word}%'
                        LIMIT 100;""")
         a = cur.fetchall()
         for i in range(len(a)):
            self.m_listCtrl2.InsertStringItem(i, a[i][0])
            self.m_listCtrl2.SetStringItem(i, 8, str(round(a[i][8], 2)))
            for j in range(1, 8):
               self.m_listCtrl2.SetStringItem(i, j, str(a[i][j]))

            if i % 2 == 0:
               self.m_listCtrl2.SetItemBackgroundColour(i, "grey")
               self.m_listCtrl2.SetItemTextColour(i, 'white')

         cur.close()
      return super().get_result(event)

   def show_item_when_click(self, event):
      idx = self.m_listCtrl2.GetFocusedItem()
      if idx != -1:
         id = self.m_listCtrl2.GetItemText(idx)
         if self.m_listCtrl2.GetColumn(0).GetText() == 'Item_ID':
            show_item(id)
         else:
            show_shop(id)
      return super().show_item_when_click(event)

app = wx.App(False)
frame = main_frame(None)
frame.Show(True)

def show_item(item_id):
   item = item_frame(None, item_id)

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()

      cur.execute('SELECT item_id, item_name, price, brand, shop_name, city, num_of_fav, num_of_sold,\
                   s5, s4, s3, s2, s1, avg_rating FROM items NATURAL JOIN shops \
                   WHERE item_id = %s;', (item.item_id,))
      a = cur.fetchone()
      rating = [i if i else 0 for i in a[8:-1]]
      print(rating)
      cur_price = a[2]
      item.SetTitle(a[0] + ' - ' + a[1])
      item.price.SetLabel('Gi?? hi???n t???i: ' + str(a[2]) + '??')
      item.brand.SetLabel('Th????ng hi???u: ' + a[3])
      item.shopname.SetLabel('Shop: ' + a[4])
      item.city.SetLabel('G???i t???: ' + a[5])
      item.fav.SetLabel('???? th??ch: ' + str(a[6]))
      item.sold.SetLabel('???? b??n: ' + str(a[7]))
      if a[-1]:
         item.rating.SetLabel('????nh gi??: ' + str(round(a[-1], 2)) + ' tr??n 5')
      else:
         item.rating.SetLabel('????nh gi??: Ch??a c?? ????nh gi??')

      cur.execute('SELECT get_item_categories(%s)', (item.item_id,))
      item.category.SetLabel('Danh m???c: ' + ' > '.join(cur.fetchone()[0].replace('Shopee.', '').split('.')))

      cur.execute('SELECT get_item_prev_price(%s);', (item.item_id,))
      prev_price = cur.fetchone()[0]
      if not prev_price:
         prev_price = cur_price

      cur.execute('SELECT MIN(price), AVG(price), MAX(price), COUNT(*)-1, MAX(date)-MIN(date) \
                   FROM item_history WHERE item_id = %s;', (item.item_id,))
      a = cur.fetchone()
      min_price = a[0]
      avg_price = a[1]
      max_price = a[2]
      item.min.SetLabel('Gi?? th???p nh???t: ' + str(min_price) + '??')
      item.avg.SetLabel('Gi?? trung b??nh: ' + str(round(avg_price, 2)) + '??')
      item.max.SetLabel('Gi?? cao nh???t: ' + str(max_price) + '??')
      item.change.SetLabel('S??? l???n thay ?????i gi??: ' + str(a[3]) + ' l???n')
      item.history.SetLabel('????? d??i l???ch s??? gi??: ' + str(a[4]) + ' ng??y')
      if cur_price <= max_price:
         item.sale1.SetLabel('So v???i gi?? cao nh???t: Gi???m ' + str(int((1 - round(cur_price/max_price, 2))*100)) + '%')
      else:
         item.sale1.SetLabel('So v???i gi?? cao nh???t: T??ng ' + str(int((round(cur_price/max_price, 2)-1)*100)) + '%')
      if cur_price <= avg_price:
         item.sale2.SetLabel('So v???i gi?? trung b??nh: Gi???m ' + str(int((1 - round(cur_price/avg_price, 2))*100)) + '%')
      else:
         item.sale2.SetLabel('So v???i gi?? trung b??nh: T??ng ' + str(int((round(cur_price/avg_price, 2)-1)*100)) + '%')
      if cur_price <= prev_price:
         item.sale3.SetLabel('So v???i gi?? g???n nh???t: Gi???m ' + str(int((1 - round(cur_price/prev_price, 2))*100)) + '%')
      else:
         item.sale3.SetLabel('So v???i gi?? g???n nh???t: T??ng ' + str(int((round(cur_price/prev_price, 2)-1)*100)) + '%')

      cur.execute('SELECT date, price FROM item_history WHERE item_id = (%s) ORDER BY date;', (item.item_id,))
      a = np.array(cur.fetchall())
      date = a[:, 0]
      price = a[:, 1]

      panel1 = CanvasPanel(item.m_panel4)
      panel1.axes.set_title('Bi???n ?????ng gi??')
      panel1.axes.plot(date, price, 'b-')
      panel1.axes.plot(date[price==min_price], min_price, 'r o')
      panel1.axes.plot(date[price==max_price], max_price, 'g o')
      panel1.axes.plot(date[price==cur_price], cur_price, 'y o')
      locator = matplotlib.ticker.MaxNLocator(nbins=5)
      panel1.axes.get_xaxis().set_major_locator(locator)
      panel1.axes.tick_params(axis='x', rotation=5)

      panel2 = CanvasPanel(item.m_panel5)
      panel2.axes.set_title('????nh gi?? s???n ph???m')
      panel2.axes.set_ylabel('S??? l?????t ????nh gi??')
      panel2.axes.bar(['5 sao', '4 sao', '3 sao', '2 sao', '1 sao'], rating, color='green')
      panel2.axes.set_ylim(0, sum(rating))
      cur.close()

   item.Show(True)

def show_shop(shop_id):
   shop = shop_frame(None, shop_id)

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()

      cur.execute('SELECT shop_id, shop_name, chat_response_rate, chat_response_time, months_of_operation, \
                   followers, city,  num_of_products, rating \
                   FROM shops WHERE shop_id = %s', (shop.shop_id,))
      a = cur.fetchone()
      shop.SetTitle(a[0] + ' - ' + a[1])
      crate = a[2]
      time = a[3]
      month = a[4]
      rank = a[8]
      shop.city.SetLabel('?????a ch???: ' + a[6])
      shop.crate.SetLabel('T??? l??? ph???n h???i chat: ' + str(int(crate*100)) + '%')
      ctime = 'Trong v??i ph??t' if a[3] == 5 else 'Trong v??i gi???' if a[3] == 4 else 'Trong v??i ng??y' if a[3] == 3 else 'Trong v??i tu???n'
      shop.ctime.SetLabel('Th???i gian ph???n h???i chat: ' + ctime)
      shop.month.SetLabel('Th???i gian tham gia: ' + str(month) + ' th??ng')
      shop.follower.SetLabel('S??? ng?????i theo d??i: ' + str(a[5]))
      shop.nums.SetLabel('S??? s???n ph???m: ' + str(a[7]))
      if rank:
         shop.rating.SetLabel('????nh gi??: ' + str(round(rank, 2)) + ' tr??n 5')
      else:
         shop.rating.SetLabel('????nh gi??: Ch??a c?? ????nh gi??')

      panel3 = CanvasPanel(shop.m_panel10)
      width = [crate*5, time, 5 if month >= 12 else month/12*5, rank]
      panel3.axes.barh(['T??? l???\n ph???n h???i', 'Th???i gian\n ph???n h???i', 'Th??m ni??n', 'X???p h???ng'], width, height=0.6, color=['orange', 'red', 'green', 'blue'])
      panel3.axes.set_title('????nh gi?? shop')

      cur.execute('SELECT SUM(s5), SUM(s4), SUM(s3), SUM(s2), SUM(s1) FROM items WHERE shop_id = %s;', (shop.shop_id,))
      rating = cur.fetchone()
      rating = [i if i else 0 for i in rating]

      panel2 = CanvasPanel(shop.m_panel8)
      panel2.axes.set_title('T???ng s??? ????nh gi??')
      panel2.axes.set_ylabel('S??? l?????t ????nh gi??')
      panel2.axes.bar(['5 sao', '4 sao', '3 sao', '2 sao', '1 sao'], rating, color='green')
      panel2.axes.set_ylim(0, sum(rating))

      cur.execute('SELECT AVG(rating), AVG(chat_response_rate), AVG(months_of_operation) \
                  FROM shops WHERE shop_id = %s;', (shop.shop_id,))
      avg_rating, avg_crate, avg_month = cur.fetchone()

      cur.execute('SELECT cal_shop_top_rating(%s), cal_shop_top_crate(%s), cal_shop_top_month(%s);', 
                     (shop.shop_id, shop.shop_id, shop.shop_id))
      top_rating, top_crate, top_month = cur.fetchone()

      shop.rank.SetLabel(f'X???p h???ng: Cao h??n {int(round(top_rating, 2)*100)}% c??c shop kh??c -- Trung b??nh: {round(avg_rating, 2)}')
      shop.crate2.SetLabel(f'T??? l??? ph???n h???i: Cao h??n {int(round(top_crate, 2)*100)}% c??c shop kh??c -- Trung b??nh: {int(round(avg_crate, 2)*100)}%')
      shop.month2.SetLabel(f'Th???i gian tham gia: Cao h??n {int(round(top_month, 2)*100)}% c??c shop kh??c -- Trung b??nh: {round(avg_month, 1)} th??ng')
      cur.close()

   shop.Show(True) 

def show_100_lowest():
   frame.m_listCtrl1.DeleteAllItems()
   frame.m_listCtrl1.DeleteAllColumns()

   frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
   frame.m_listCtrl1.InsertColumn(1, 'Name')
   frame.m_listCtrl1.InsertColumn(2, 'Price')

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()
      cur.execute('SELECT * FROM show_top_n_lowest_item(%s);', (100,))
      a = cur.fetchall()
      for i in range(len(a)):
         frame.m_listCtrl1.InsertStringItem(i, a[i][0])
         frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
         frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
         if i % 2 == 0:
            frame.m_listCtrl1.SetItemBackgroundColour(i, "grey")  
            frame.m_listCtrl1.SetItemTextColour(i, 'white')
      cur.close()

def show_100_highest():
   frame.m_listCtrl1.DeleteAllItems()
   frame.m_listCtrl1.DeleteAllColumns()

   frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
   frame.m_listCtrl1.InsertColumn(1, 'Name')
   frame.m_listCtrl1.InsertColumn(2, 'Price')

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()
      cur.execute('SELECT * FROM show_top_n_highest_item(%s);', (100,))
      a = cur.fetchall()
      for i in range(len(a)):
         frame.m_listCtrl1.InsertStringItem(i, a[i][0])
         frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
         frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
         if i % 2 == 0:
            frame.m_listCtrl1.SetItemBackgroundColour(i, "grey")
            frame.m_listCtrl1.SetItemTextColour(i, 'white')
      cur.close()

def show_100_fav_HN():
   frame.m_listCtrl1.DeleteAllItems()
   frame.m_listCtrl1.DeleteAllColumns()

   frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
   frame.m_listCtrl1.InsertColumn(1, 'Name')
   frame.m_listCtrl1.InsertColumn(2, 'Price')
   frame.m_listCtrl1.InsertColumn(3, 'Category')
   frame.m_listCtrl1.InsertColumn(4, 'Shop')
   frame.m_listCtrl1.InsertColumn(5, 'Favourite')
   frame.m_listCtrl1.InsertColumn(6, 'Sold')
   frame.m_listCtrl1.InsertColumn(7, 'Rating')

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()
      cur.execute("""SELECT item_id, item_name, price, category_name, shop_name, num_of_fav, num_of_sold, avg_rating
                     FROM items
                        NATURAL JOIN categories
                        NATURAL JOIN shops
                        NATURAL JOIN (SELECT category_id, MAX(num_of_fav) as most_fav
                                    FROM items NATURAL JOIN shops
                                    WHERE city = 'H?? N???i'
                                    GROUP BY category_id) p
                     WHERE num_of_fav = most_fav;""")
      a = cur.fetchall()
      for i in range(len(a)):
         frame.m_listCtrl1.InsertStringItem(i, a[i][0])
         frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
         frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
         frame.m_listCtrl1.SetStringItem(i, 3, a[i][3])
         frame.m_listCtrl1.SetStringItem(i, 4, a[i][4])
         frame.m_listCtrl1.SetStringItem(i, 5, str(a[i][5]))
         frame.m_listCtrl1.SetStringItem(i, 6, str(a[i][6]))
         frame.m_listCtrl1.SetStringItem(i, 7, str(round(a[i][7], 2)))
         if i % 2 == 0:
            frame.m_listCtrl1.SetItemBackgroundColour(i, "pink")
            frame.m_listCtrl1.SetItemTextColour(i, 'grey')
      cur.close()

def show_all_shops_by_rating():
   frame.m_listCtrl1.DeleteAllItems()
   frame.m_listCtrl1.DeleteAllColumns()

   frame.m_listCtrl1.InsertColumn(0, 'Shop_ID')
   frame.m_listCtrl1.InsertColumn(1, 'Name')
   frame.m_listCtrl1.InsertColumn(2, 'Price')

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()
      cur.execute('SELECT shop_id, shop_name, rating FROM shops ORDER BY rating DESC;')
      a = cur.fetchall()
      for i in range(len(a)):
         frame.m_listCtrl1.InsertStringItem(i, a[i][0])
         frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
         frame.m_listCtrl1.SetStringItem(i, 2, str(round(a[i][2], 2)))
         if i % 2 == 0:
            frame.m_listCtrl1.SetItemBackgroundColour(i, "grey")
            frame.m_listCtrl1.SetItemTextColour(i, 'white')
      cur.close()

def show_SRM():
   frame.m_listCtrl1.DeleteAllItems()
   frame.m_listCtrl1.DeleteAllColumns()

   frame.m_listCtrl1.InsertColumn(0, 'Item_ID')
   frame.m_listCtrl1.InsertColumn(1, 'Name')
   frame.m_listCtrl1.InsertColumn(2, 'Number of sold products')
   frame.m_listCtrl1.InsertColumn(3, 'Price')

   with psycopg2.connect(host=host,
                        database=database,
                        user=user,
                        password=password,
                        port=port) as conn:
      cur = conn.cursor()
      cur.execute('''SELECT item_id, item_name, num_of_sold, price
                     FROM items, categories
                     WHERE items.category_id = categories.category_id
                     AND category_name = \'S???a r???a m???t\'
                     ORDER BY num_of_sold DESC;''')
      a = cur.fetchall()
      for i in range(len(a)):
         frame.m_listCtrl1.InsertStringItem(i, a[i][0])
         frame.m_listCtrl1.SetStringItem(i, 1, a[i][1])
         frame.m_listCtrl1.SetStringItem(i, 2, str(a[i][2]))
         frame.m_listCtrl1.SetStringItem(i, 3, str(a[i][3]))
         if i % 2 == 0:
            frame.m_listCtrl1.SetItemBackgroundColour(i, "blue")
            frame.m_listCtrl1.SetItemTextColour(i, 'white')
      cur.close()   

def show_item_search():
   search = search_frame(None)
   search.m_searchCtrl1.SetMaxLength(210)
   search.Show(True)

#start the applications
app.MainLoop()