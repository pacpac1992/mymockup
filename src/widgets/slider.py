#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.lib.ogl as ogl

class Dialog_Slider(wx.Dialog):
	def __init__(self, parent, title):
		super(Dialog_Slider, self).__init__(parent, title=title,size=(260,150))
		self.parent = parent
		
		wx.StaticText(self,-1,'Size:',pos=(10,10),size=(50,30))
		
		rotate = ["Horizontal","Vertical"]

		self.size_cbo_img = wx.ComboBox(self, -1, value="Horizontal", pos=(60,5),size=(150,30), choices=rotate)

		btn = wx.Button(self,-1,'Aceptar',pos=(60,40))

		btn.Bind(wx.EVT_BUTTON,self.size)

	def size(self,evt):
		ang = self.size_cbo_img.GetValue()
		self.parent.draw_slider(None,ang)
		self.Destroy()

class Slider(ogl.CompositeShape):
	
	def __init__(self, canvas,img,rotate = "Horizontal"):
		ogl.CompositeShape.__init__(self)

		self.SetCanvas(canvas)

		constraining_shape = ogl.BitmapShape()
		constraining_shape.SetBitmap(wx.Bitmap( img, wx.BITMAP_TYPE_ANY ))
		if rotate == "Horizontal":
			constrained_shape1 = ogl.RectangleShape(100, 2)
		else:
			constrained_shape1 = ogl.RectangleShape(2, 100)

		self.AddChild(constrained_shape1)
		self.AddChild(constraining_shape)

		constraint = ogl.Constraint(ogl.CONSTRAINT_CENTRED_BOTH, constraining_shape, [constrained_shape1])
		self.AddConstraint(constraint)

		self.Recompute()

		# If we don't do this, the shapes will be able to move on their
		# own, instead of moving the composite
		constraining_shape.SetDraggable(False)
		constrained_shape1.SetDraggable(False)

		# If we don't do this the shape will take all left-clicks for itself
		constraining_shape.SetSensitivityFilter(0)