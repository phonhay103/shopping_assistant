# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

item_category = 1000
item_price = 1001
item_brand = 1002
item_shop = 1003
item_fav = 1004
item_sold = 1005
item_city = 1006
item_rating = 1007
item_min = 1008
item_avg = 1009
item_max = 1010
item_num_changes = 1011
history = 1012

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Trợ lý mua sắm", pos = wx.DefaultPosition, size = wx.Size( 1376,780 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1376,780 ), wx.Size( 1376,780 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button9 = wx.Button( self.m_panel11, wx.ID_ANY, u"Search Item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button9, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button12 = wx.Button( self.m_panel11, wx.ID_ANY, u"Search Demo", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.RandomItem = wx.Button( self.m_panel11, wx.ID_ANY, u"Pick a random item", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.RandomItem, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.RandomShop = wx.Button( self.m_panel11, wx.ID_ANY, u"Pick a random shop", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.RandomShop, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.lowest_price_100 = wx.Button( self.m_panel11, wx.ID_ANY, u"100 lowest price items", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.lowest_price_100, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.highest_price_100 = wx.Button( self.m_panel11, wx.ID_ANY, u"100 highest price items", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.highest_price_100, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.sss = wx.Button( self.m_panel11, wx.ID_ANY, u"Show shops by rating", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.sss, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button6 = wx.Button( self.m_panel11, wx.ID_ANY, u"Most favourite per category in HaNoi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button6, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button7 = wx.Button( self.m_panel11, wx.ID_ANY, u"Product 'Sữa rửa mặt' sort by number of products sold", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button7, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button8 = wx.Button( self.m_panel11, wx.ID_ANY, u"Sản phẩm: 'Kem và sữa dưỡng da', 'Tp. Hồ Chí Minh', Mức giá từ 50.000đ đến 500.000đ", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button8, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel11.SetSizer( bSizer8 )
		self.m_panel11.Layout()
		bSizer8.Fit( self.m_panel11 )
		gSizer3.Add( self.m_panel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer81 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl1 = wx.ListCtrl( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.Size( 660,780 ), wx.LC_AUTOARRANGE|wx.LC_REPORT )
		bSizer81.Add( self.m_listCtrl1, 0, wx.ALL, 5 )
		
		
		self.m_panel12.SetSizer( bSizer81 )
		self.m_panel12.Layout()
		bSizer81.Fit( self.m_panel12 )
		gSizer3.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button9.Bind( wx.EVT_BUTTON, self.item_search )
		self.m_button12.Bind( wx.EVT_BUTTON, self.Demo )
		self.RandomItem.Bind( wx.EVT_BUTTON, self.random_item )
		self.RandomShop.Bind( wx.EVT_BUTTON, self.random_shop )
		self.lowest_price_100.Bind( wx.EVT_BUTTON, self.show_all_items )
		self.highest_price_100.Bind( wx.EVT_BUTTON, self.show_all_items2 )
		self.sss.Bind( wx.EVT_BUTTON, self.show_shops_by_rating )
		self.m_button6.Bind( wx.EVT_BUTTON, self.top_100_fav_HN )
		self.m_button7.Bind( wx.EVT_BUTTON, self.SRM )
		self.m_button8.Bind( wx.EVT_BUTTON, self.button8 )
		self.m_listCtrl1.Bind( wx.EVT_LIST_ITEM_SELECTED, self.show_item_when_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def item_search( self, event ):
		event.Skip()
	
	def Demo( self, event ):
		event.Skip()
	
	def random_item( self, event ):
		event.Skip()
	
	def random_shop( self, event ):
		event.Skip()
	
	def show_all_items( self, event ):
		event.Skip()
	
	def show_all_items2( self, event ):
		event.Skip()
	
	def show_shops_by_rating( self, event ):
		event.Skip()
	
	def top_100_fav_HN( self, event ):
		event.Skip()
	
	def SRM( self, event ):
		event.Skip()
	
	def button8( self, event ):
		event.Skip()
	
	def show_item_when_click( self, event ):
		event.Skip()
	

###########################################################################
## Class Item
###########################################################################

class Item ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Item_name", pos = wx.DefaultPosition, size = wx.Size( 1376,780 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1376,780 ), wx.Size( 1376,780 ) )
		self.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.category = wx.StaticText( self.m_panel1, item_category, u"category", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.category.Wrap( -1 )
		self.category.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.category.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer5.Add( self.category, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.price = wx.StaticText( self.m_panel1, item_price, u"price", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.price.Wrap( -1 )
		self.price.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.price.SetForegroundColour( wx.Colour( 255, 255, 0 ) )
		self.price.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer5.Add( self.price, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.brand = wx.StaticText( self.m_panel1, item_brand, u"brand", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.brand.Wrap( -1 )
		self.brand.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.brand.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer5.Add( self.brand, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.shopname = wx.StaticText( self.m_panel1, item_shop, u"shopname", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.shopname.Wrap( -1 )
		self.shopname.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.shopname.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer5.Add( self.shopname, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.fav = wx.StaticText( self.m_panel1, item_fav, u"fav", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.fav.Wrap( -1 )
		self.fav.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.fav.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer5.Add( self.fav, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.sold = wx.StaticText( self.m_panel1, item_sold, u"sold", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.sold.Wrap( -1 )
		self.sold.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.sold.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer5.Add( self.sold, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.city = wx.StaticText( self.m_panel1, item_city, u"city", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.city.Wrap( -1 )
		self.city.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.city.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer5.Add( self.city, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.rating = wx.StaticText( self.m_panel1, item_rating, u"rating", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.rating.Wrap( -1 )
		self.rating.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.rating.SetForegroundColour( wx.Colour( 128, 255, 128 ) )
		self.rating.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer5.Add( self.rating, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		gSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel3 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.min = wx.StaticText( self.m_panel3, item_min, u"min", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.min.Wrap( -1 )
		self.min.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.min.SetForegroundColour( wx.Colour( 255, 0, 0 ) )
		
		bSizer7.Add( self.min, 0, wx.ALL, 5 )
		
		self.avg = wx.StaticText( self.m_panel3, item_avg, u"avg", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.avg.Wrap( -1 )
		self.avg.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.avg, 0, wx.ALL, 5 )
		
		self.max = wx.StaticText( self.m_panel3, item_max, u"max", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.max.Wrap( -1 )
		self.max.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.max.SetForegroundColour( wx.Colour( 0, 128, 0 ) )
		
		bSizer7.Add( self.max, 0, wx.ALL, 5 )
		
		self.change = wx.StaticText( self.m_panel3, item_num_changes, u"change", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.change.Wrap( -1 )
		self.change.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.change, 0, wx.ALL, 5 )
		
		self.history = wx.StaticText( self.m_panel3, history, u"history", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.history.Wrap( -1 )
		self.history.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.history, 0, wx.ALL, 5 )
		
		self.sale1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sale1.Wrap( -1 )
		self.sale1.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.sale1, 0, wx.ALL, 5 )
		
		self.sale2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"sale2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sale2.Wrap( -1 )
		self.sale2.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.sale2, 0, wx.ALL, 5 )
		
		self.sale3 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"sale3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sale3.Wrap( -1 )
		self.sale3.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer7.Add( self.sale3, 0, wx.ALL, 5 )
		
		
		self.m_panel3.SetSizer( bSizer7 )
		self.m_panel3.Layout()
		bSizer7.Fit( self.m_panel3 )
		bSizer6.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,460 ), wx.TAB_TRAVERSAL )
		bSizer6.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer6 )
		self.m_panel2.Layout()
		bSizer6.Fit( self.m_panel2 )
		gSizer2.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.brand.Bind( wx.EVT_LEFT_DOWN, self.brand_click )
		self.shopname.Bind( wx.EVT_LEFT_DOWN, self.click_on_shopname )
		self.city.Bind( wx.EVT_LEFT_DOWN, self.city_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def brand_click( self, event ):
		event.Skip()
	
	def click_on_shopname( self, event ):
		event.Skip()
	
	def city_click( self, event ):
		event.Skip()
	

###########################################################################
## Class Shop
###########################################################################

class Shop ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1376,780 ), style = wx.DEFAULT_FRAME_STYLE|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1376,780 ), wx.Size( 1376,780 ) )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.nums = wx.StaticText( self.m_panel6, wx.ID_ANY, u"nums", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nums.Wrap( -1 )
		bSizer4.Add( self.nums, 0, wx.ALL, 5 )
		
		self.month = wx.StaticText( self.m_panel6, wx.ID_ANY, u"month", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.month.Wrap( -1 )
		bSizer4.Add( self.month, 0, wx.ALL, 5 )
		
		self.crate = wx.StaticText( self.m_panel6, wx.ID_ANY, u"crate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.crate.Wrap( -1 )
		bSizer4.Add( self.crate, 0, wx.ALL, 5 )
		
		self.ctime = wx.StaticText( self.m_panel6, wx.ID_ANY, u"ctime", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ctime.Wrap( -1 )
		bSizer4.Add( self.ctime, 0, wx.ALL, 5 )
		
		self.follower = wx.StaticText( self.m_panel6, wx.ID_ANY, u"follower", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.follower.Wrap( -1 )
		bSizer4.Add( self.follower, 0, wx.ALL, 5 )
		
		self.city = wx.StaticText( self.m_panel6, wx.ID_ANY, u"city", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.city.Wrap( -1 )
		bSizer4.Add( self.city, 0, wx.ALL, 5 )
		
		self.rating = wx.StaticText( self.m_panel6, wx.ID_ANY, u"rating", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rating.Wrap( -1 )
		bSizer4.Add( self.rating, 0, wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( bSizer4 )
		self.m_panel6.Layout()
		bSizer4.Fit( self.m_panel6 )
		gSizer2.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel9 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.rank = wx.StaticText( self.m_panel9, wx.ID_ANY, u"rank", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rank.Wrap( -1 )
		bSizer7.Add( self.rank, 0, wx.ALL, 5 )
		
		self.crate2 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"crate2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.crate2.Wrap( -1 )
		bSizer7.Add( self.crate2, 0, wx.ALL, 5 )
		
		self.month2 = wx.StaticText( self.m_panel9, wx.ID_ANY, u"month2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.month2.Wrap( -1 )
		bSizer7.Add( self.month2, 0, wx.ALL, 5 )
		
		
		self.m_panel9.SetSizer( bSizer7 )
		self.m_panel9.Layout()
		bSizer7.Fit( self.m_panel9 )
		bSizer5.Add( self.m_panel9, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel10 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,497 ), wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel7.SetSizer( bSizer5 )
		self.m_panel7.Layout()
		bSizer5.Fit( self.m_panel7 )
		gSizer2.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ItemSearch
###########################################################################

class ItemSearch ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tìm Kiếm Sản Phẩm", pos = wx.DefaultPosition, size = wx.Size( 1376,780 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 1376,780 ), wx.Size( 1376,780 ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		self.m_searchCtrl1.SetFont( wx.Font( 14, 74, 90, 90, False, "Arial Rounded MT Bold" ) )
		
		bSizer12.Add( self.m_searchCtrl1, 0, wx.ALL|wx.EXPAND, 5 )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, u"Sort By" ), wx.VERTICAL )
		
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.PriceSort = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Price", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PriceSort.Wrap( -1 )
		gSizer7.Add( self.PriceSort, 0, wx.ALL, 5 )
		
		m_choice2Choices = [ u"None", u"Ascending", u"Descending" ]
		self.m_choice2 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
		self.m_choice2.SetSelection( 1 )
		gSizer7.Add( self.m_choice2, 0, wx.ALL, 5 )
		
		self.FavSort = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Num of favourites", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FavSort.Wrap( -1 )
		gSizer7.Add( self.FavSort, 0, wx.ALL, 5 )
		
		m_choice3Choices = [ u"None", u"Ascending", u"Descending" ]
		self.m_choice3 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		gSizer7.Add( self.m_choice3, 0, wx.ALL, 5 )
		
		self.SoldSort = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Num of sold products", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SoldSort.Wrap( -1 )
		gSizer7.Add( self.SoldSort, 0, wx.ALL, 5 )
		
		m_choice4Choices = [ u"None", u"Ascending", u"Descending" ]
		self.m_choice4 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		gSizer7.Add( self.m_choice4, 0, wx.ALL, 5 )
		
		self.RatingSort = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Rating", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RatingSort.Wrap( -1 )
		gSizer7.Add( self.RatingSort, 0, wx.ALL, 5 )
		
		m_choice5Choices = [ u"None", u"Ascending", u"Descending" ]
		self.m_choice5 = wx.Choice( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice5Choices, 0 )
		self.m_choice5.SetSelection( 2 )
		gSizer7.Add( self.m_choice5, 0, wx.ALL, 5 )
		
		
		sbSizer4.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, u"Price Range" ), wx.VERTICAL )
		
		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_textCtrl1 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"30000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, u"80000", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer8.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer8, 1, wx.EXPAND, 5 )
		
		
		bSizer14.Add( sbSizer5, 1, wx.EXPAND, 5 )
		
		sbSizer6 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, u"City" ), wx.VERTICAL )
		
		m_choice13Choices = [ u"None", u"Hà Nội", u"Tp. Hồ Chí Minh", u"Nước Ngoài", u"Hải Dương", u"Nước Ngoài", u"Hải Phòng", u"Quảng Ninh", u"Nam Định", u"Ninh Bình", u"Hà Nam" ]
		self.m_choice13 = wx.Choice( sbSizer6.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice13Choices, 0 )
		self.m_choice13.SetSelection( 0 )
		sbSizer6.Add( self.m_choice13, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( sbSizer6, 1, wx.EXPAND, 5 )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel13, wx.ID_ANY, u"Rating" ), wx.VERTICAL )
		
		m_choice14Choices = [ u"None", u"5.0", u"4.0", u"3.0", u"2.0", u"1.0" ]
		self.m_choice14 = wx.Choice( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice14Choices, 0 )
		self.m_choice14.SetSelection( 0 )
		sbSizer7.Add( self.m_choice14, 0, wx.ALL, 5 )
		
		
		bSizer14.Add( sbSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel13.SetSizer( bSizer14 )
		self.m_panel13.Layout()
		bSizer14.Fit( self.m_panel13 )
		gSizer6.Add( self.m_panel13, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel14 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_listCtrl2 = wx.ListCtrl( self.m_panel14, wx.ID_ANY, wx.DefaultPosition, wx.Size( 660,780 ), wx.LC_REPORT )
		self.m_listCtrl2.SetFont( wx.Font( 10, 74, 90, 90, False, "Arial" ) )
		self.m_listCtrl2.SetMinSize( wx.Size( 660,780 ) )
		self.m_listCtrl2.SetMaxSize( wx.Size( 660,780 ) )
		
		bSizer13.Add( self.m_listCtrl2, 0, wx.ALL, 5 )
		
		
		self.m_panel14.SetSizer( bSizer13 )
		self.m_panel14.Layout()
		bSizer13.Fit( self.m_panel14 )
		gSizer6.Add( self.m_panel14, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer12.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_searchCtrl1.Bind( wx.EVT_SEARCHCTRL_SEARCH_BTN, self.get_result )
		self.m_listCtrl2.Bind( wx.EVT_LIST_ITEM_SELECTED, self.show_item_when_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def get_result( self, event ):
		event.Skip()
	
	def show_item_when_click( self, event ):
		event.Skip()
	

