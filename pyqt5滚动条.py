import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        main_window = QWidget()             # 主窗口
        main_window_layout = QHBoxLayout()  # 用于设置主窗口的布局
        body_wrap = QScrollArea()           # 滚动区域。想要实现滚动区域，就是要声明一个 QScrollArea 控件，并让它包裹想要滚动的窗体
        body = QWidget()                    # 主窗口中真正装载内容的窗口（body_wrap 就是用来包裹它的）。是带有滚动条的区域

        self.setCentralWidget(main_window)        # 设置 main_window 为当前窗口的中心窗体
        main_window.setFixedSize(1200, 800)       # 设置 main_window 为固定宽高（这只是我个人的喜好，在本例中可以删除）
        main_window.setLayout(main_window_layout) # 设置 main_window 的布局模式。（以上都是常规、不带滚动条的代码）
        body.setMinimumSize(1100, 900)            # 设置内容区域（滚动区域）的最小 size。必须比前面 main_window 的要大
        body_wrap.setWidget(body)                 # 用 body_wrap 包裹内容区域。（包裹只是我个人为了理解的创造性说法）
        main_window_layout.addWidget(body_wrap)   # 在 main_window 的布局中加入可滚动区域，大功告成。

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())
