import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QToolBar, QAction, QTreeWidget, QTreeWidgetItem, QTabWidget,
    QWidget, QGridLayout, QLabel, QVBoxLayout, QTextEdit, QPushButton, QScrollArea, QProgressBar, QStatusBar,
    QSplitter
)
from PyQt5.QtCore import Qt

data = {
    "comparison": {
        "bar-chart": {
            "vertical": ["vbar1", "vbar2"],
            "horizontal": ["vbar1", "vbar2"],
            "clustered": ["cbar1", "cbar2"],
            "stacked": ["ebar1", "ebar2"]
        },
        "radar-diagram": ["rdiag1", "rdiag2"],
        "bubble-chart": ["bchart1", "bchart2"]
    },
    "distribution": {
        "histogram": ["hist1", "hist2"],
        "boxplot": ["boxp1", "boxp2"],
        "violin": ["viol1", "viol2"]
    },
    "composition": {
        "piechart": ["piechart1", "piechart2"],
        "stacked-area": ["sarea1", "sarea2"],
        "treemap": ["treemap1", "treemap2"]
    },
    "relation": {
        "scatter-plot": ["scatter1", "scatter2"],
        "correlation-plot": ["corr1", "corr2"],
        "network-diagram": ["net1", "net2"]
    },
    "process": {
        "flowchart": ["flowchart1", "flowchart2"],
        "gantt": ["gantt1", "gantt2"],
        "bpmn": ["bpmn1", "bpmn2"]
    },
    "strategy": {
        "swot": ["swot1", "swot2"],
        "bcg": ["bcg1", "bcg2"],
        "ansoff": ["ansoff1", "ansoff2"]
    }
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 GUI")
        self.setGeometry(100, 100, 800, 600)
        
        self.toolbar = QToolBar("Toolbar")
        self.addToolBar(self.toolbar)
        
        about_action = QAction("About", self)
        about_action.triggered.connect(lambda: print("about"))
        self.toolbar.addAction(about_action)
        
        coffee_action = QAction("Coffee", self)
        coffee_action.triggered.connect(lambda: print("Buy me a coffee"))
        self.toolbar.addAction(coffee_action)
        
        configure_action = QAction("Configure", self)
        configure_action.triggered.connect(lambda: print("Configure"))
        self.toolbar.addAction(configure_action)
        
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.populate_tree(self.tree, data)
        self.tree.itemClicked.connect(self.on_tree_item_clicked)
        
        self.tabs = QTabWidget()
        self.create_tabs()
        
        self.splitter = QSplitter()
        self.splitter.addWidget(self.tree)
        self.splitter.addWidget(self.tabs)
        self.splitter.setSizes([200, 600])
        
        self.progress_bar = QProgressBar()
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.splitter)
        main_layout.addWidget(self.progress_bar)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def populate_tree(self, parent, data):
        for key, value in data.items():
            item = QTreeWidgetItem([key])
            parent.addTopLevelItem(item) if isinstance(parent, QTreeWidget) else parent.addChild(item)
            if isinstance(value, dict):
                self.populate_tree(item, value)
            elif isinstance(value, list):
                for leaf in value:
                    item.addChild(QTreeWidgetItem([leaf]))
    
    def on_tree_item_clicked(self, item):
        leaves = []
        self.collect_leaves(item, leaves)
        print(leaves)
    
    def collect_leaves(self, item, leaves):
        if item.childCount() == 0:
            leaves.append(item.text(0))
        else:
            for i in range(item.childCount()):
                self.collect_leaves(item.child(i), leaves)
    
    def create_tabs(self):
        self.image_tab = QWidget()
        grid_layout = QGridLayout()
        images = [f"image_{i}.png" for i in range(6)]
        for idx, img in enumerate(images):
            label = QLabel(img)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.mouseDoubleClickEvent = lambda event, img=img: print(img)
            grid_layout.addWidget(label, idx // 3, idx % 3)
        self.image_tab.setLayout(grid_layout)
        
        self.detail_tab = QWidget()
        detail_layout = QVBoxLayout()
        
        scroll_area = QScrollArea()
        large_image = QLabel("Large Image Here")
        scroll_area.setWidget(large_image)
        scroll_area.setWidgetResizable(True)
        
        text_edit = QTextEdit()
        text_edit.setPlaceholderText("Details...")
        
        button_layout = QVBoxLayout()
        consult_btn = QPushButton("Consult")
        download_img_btn = QPushButton("Download Image")
        download_code_btn = QPushButton("Download Code")
        
        button_layout.addWidget(consult_btn)
        button_layout.addWidget(download_img_btn)
        button_layout.addWidget(download_code_btn)
        
        detail_layout.addWidget(scroll_area)
        detail_layout.addWidget(text_edit)
        detail_layout.addLayout(button_layout)
        self.detail_tab.setLayout(detail_layout)
        
        self.tabs.addTab(self.image_tab, "Images")
        self.tabs.addTab(self.detail_tab, "Details")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

