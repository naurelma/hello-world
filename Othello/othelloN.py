import sys
from PyQt5.QtCore import Qt,QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QHBoxLayout

from PyQt5.QtGui import QPainter, QColor, QBrush,QPen
import othello


class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):      
		
		grid = QGridLayout()
		grid.setSpacing(10)
		self.offset = 30
		self.sivu = 10
		
		x = 0
		y = 0
		self.lauta = othello.luo()
		self.vuoro = -1
		self.text = "x: {0},  y: {1},V: {2}".format(x, y, self.vuoro)
		
		self.label = QLabel(self.text, self)
		grid.addWidget(self.label, 0, 0, Qt.AlignTop)
		

		
		self.setLayout(grid)
		
		self.setGeometry(300, 20, 1000, 1000)
		self.setWindowTitle('Othello')
		self.show()
		
	def move(self,x,y):
		if self.lauta.aseta((x,y),self.vuoro):
			self.vuoro *= -1


	def mousePressEvent(self, e):
		
		x = int((e.x() - self.offset)//self.sivu)
		y = int((e.y() - self.offset)//self.sivu)


		if x >= 0 and y>= 0 and x<8 and y<8:
			self.move(x,y)
			self.text = "x: {0},  y: {1},V: {2}, S: {3}".format(x, y, self.vuoro, self.lauta.summa())
			self.label.setText(self.text)
			self.update()

	
	def paintEvent(self, e):

		qp = QPainter()
		qp.begin(self)
		self.drawGrid(qp)
		self.näytä(qp)
		self.lailliset(qp)
		qp.end()

	def lailliset(self,qp):
		def neliö(x,y):
			s = self.sivu-8
			x += 4
			y += 4
			qp.drawLine(x, y, x+s, y)
			qp.drawLine(x+s, y, x+s, y+s)
			qp.drawLine(x+s, y+s, x, y+s)
			qp.drawLine(x, y+s, x, y)
		qp.setBrush(QColor(0, 255, 0))
		p = QPen()
		p.setWidth(6)
		qp.setPen(p)
		la = self.lauta.lailliset(self.vuoro)
		if len(la) == 0:
			self.vuoro *= -1
		for i in la:
			x,y = i[0],i[1]
			x = x*self.sivu + self.offset
			y = y*self.sivu + self.offset
			neliö(x,y)

	def näytä(self,qp):
		def ympyrä(x,y):
			x = x*self.sivu + self.offset + self.sivu//2
			y = y*self.sivu + self.offset + self.sivu//2
			qp.drawEllipse(QPoint(x,y),self.sivu//3,self.sivu//3)
		for i in range(8):
			for j in range(8):
				nappi = self.lauta[(j,i)]
				if nappi == 0:
					continue
				elif nappi == 1:
					qp.setBrush(QColor(255, 255, 255))
					ympyrä(j,i)
				elif nappi == -1:
					qp.setBrush(QColor(0, 0, 0))
					ympyrä(j,i)

	def drawGrid(self, qp):
	  
		col = QColor(0, 0, 0)
		col.setNamedColor('#d4d4d4')
		qp.setPen(col)
		total = min(self.contentsRect().width(),self.contentsRect().height())

		sivu = (total - self.offset*2)/8
		self.sivu = sivu

		def neliö(x,y):
			qp.drawRect(self.offset+x, self.offset+y,sivu,sivu)

		for i in range(8):
			for j in range(4):
				qp.setBrush(QColor(255, 50, 50))
				neliö(sivu*i, 2*sivu*j + sivu*(i%2))

				qp.setBrush(QColor(50, 50, 255))
				neliö(sivu*i, 2*sivu*j + sivu*((i+1)%2))
				  
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())