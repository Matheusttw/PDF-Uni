import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QSpinBox, QMessageBox, QFileDialog, QHBoxLayout,
    QCheckBox, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PDFEditorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P D F Uni")
        self.setGeometry(100, 100, 200, 200)  # Janela larga e alta para duas colunas

        # Ativa tema escuro por padrão
        self.dark_mode = True 
        self.set_dark_theme()

        # Layout principal vertical (contém título e o layout horizontal de colunas)
        main_layout = QVBoxLayout()

        # Alternância de tema escuro
        self.theme_toggle = QCheckBox("Skin Dark")
        self.theme_toggle.setChecked(True)
        self.theme_toggle.stateChanged.connect(self.toggle_theme)
        main_layout.addWidget(self.theme_toggle, alignment=Qt.AlignLeft)

        # Título em cor bordô
        header_label = QLabel("PDF Uni")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet("color: #C00000; font-size: 20px; padding: 5px;")
        main_layout.addWidget(header_label)

        # Layout horizontal com duas colunas
        columns_layout = QHBoxLayout()
        left_column = QVBoxLayout()   # Coluna esquerda: Unir e Dividir
        right_column = QVBoxLayout()  # Coluna direita: Rotacionar

        # ------------------- COLUNA ESQUERDA -------------------

        # Seção Unir PDFs
        self.label = QLabel("Selecione a pasta com os PDFs:")
        self.label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.label)

        self.select_button = QPushButton("Selecionar Pasta")
        self.select_button.clicked.connect(self.select_folder)
        left_column.addWidget(self.select_button, alignment=Qt.AlignCenter)

        self.merge_label = QLabel("Nome do PDF Unido:")
        self.merge_label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.merge_label)

        self.merge_name_entry = QLineEdit()
        self.merge_name_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.merge_name_entry.setMinimumHeight(30)
        left_column.addWidget(self.merge_name_entry, alignment=Qt.AlignCenter)

        self.merge_button = QPushButton("Unir PDFs")
        self.merge_button.clicked.connect(self.merge_pdfs)
        self.merge_button.setEnabled(False)
        left_column.addWidget(self.merge_button, alignment=Qt.AlignCenter)

        # Seção Dividir PDF
        self.split_label = QLabel("Selecionar PDF para Dividir:")
        self.split_label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.split_label)

        self.pdf_file_label = QLabel("Nenhum PDF selecionado")
        self.pdf_file_label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.pdf_file_label)

        self.select_pdf_button = QPushButton("Selecionar PDF")
        self.select_pdf_button.clicked.connect(self.select_pdf)
        self.select_pdf_button.setEnabled(False)
        left_column.addWidget(self.select_pdf_button, alignment=Qt.AlignCenter)

        self.start_page_label = QLabel("Página Inicial:")
        self.start_page_label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.start_page_label)

        self.start_page_spinbox = QSpinBox()
        self.start_page_spinbox.setRange(1, 1000)
        self.start_page_spinbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        left_column.addWidget(self.start_page_spinbox, alignment=Qt.AlignCenter)

        self.end_page_label = QLabel("Página Final:")
        self.end_page_label.setAlignment(Qt.AlignCenter)
        left_column.addWidget(self.end_page_label)

        self.end_page_spinbox = QSpinBox()
        self.end_page_spinbox.setRange(1, 1000)
        self.end_page_spinbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        left_column.addWidget(self.end_page_spinbox, alignment=Qt.AlignCenter)

        self.split_button = QPushButton("Dividir PDF")
        self.split_button.clicked.connect(self.split_pdf)
        self.split_button.setEnabled(False)
        left_column.addWidget(self.split_button, alignment=Qt.AlignCenter)

        left_column.addStretch()

        # ------------------- COLUNA DIREITA -------------------

        # Seção Rotacionar Página
        self.rotate_label = QLabel("Selecionar PDF para Rotacionar:")
        self.rotate_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotate_label)

        self.rotate_pdf_file_label = QLabel("Nenhum PDF selecionado")
        self.rotate_pdf_file_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotate_pdf_file_label)

        self.select_rotate_pdf_button = QPushButton("Selecionar PDF")
        self.select_rotate_pdf_button.clicked.connect(self.select_rotate_pdf)
        self.select_rotate_pdf_button.setEnabled(False)
        right_column.addWidget(self.select_rotate_pdf_button, alignment=Qt.AlignCenter)

        self.page_to_rotate_label = QLabel("Página para Rotacionar:")
        self.page_to_rotate_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.page_to_rotate_label)

        self.page_to_rotate_spinbox = QSpinBox()
        self.page_to_rotate_spinbox.setRange(1, 1000)
        self.page_to_rotate_spinbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        right_column.addWidget(self.page_to_rotate_spinbox, alignment=Qt.AlignCenter)

        self.rotation_angle_label = QLabel("Ângulo (graus):")
        self.rotation_angle_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotation_angle_label)

        self.rotation_angle_spinbox = QSpinBox()
        self.rotation_angle_spinbox.setRange(90, 270)
        self.rotation_angle_spinbox.setSingleStep(90)
        self.rotation_angle_spinbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        right_column.addWidget(self.rotation_angle_spinbox, alignment=Qt.AlignCenter)

        self.rotate_button = QPushButton("Aplicar Rotação")
        self.rotate_button.clicked.connect(self.rotate_pdf)
        self.rotate_button.setEnabled(False)
        right_column.addWidget(self.rotate_button, alignment=Qt.AlignCenter)

        # Seção Rotacionar PDF Inteiro
        self.rotate_all_label = QLabel("Rotacionar PDF Completo:")
        self.rotate_all_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotate_all_label)

        self.rotate_all_pdf_label = QLabel("Nenhum PDF selecionado")
        self.rotate_all_pdf_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotate_all_pdf_label)

        self.select_rotate_all_pdf_button = QPushButton("Selecionar PDF")
        self.select_rotate_all_pdf_button.clicked.connect(self.select_rotate_all_pdf)
        self.select_rotate_all_pdf_button.setEnabled(False)
        right_column.addWidget(self.select_rotate_all_pdf_button, alignment=Qt.AlignCenter)

        self.rotation_all_angle_label = QLabel("Ângulo (graus):")
        self.rotation_all_angle_label.setAlignment(Qt.AlignCenter)
        right_column.addWidget(self.rotation_all_angle_label)

        self.rotation_all_angle_spinbox = QSpinBox()
        self.rotation_all_angle_spinbox.setRange(90, 270)
        self.rotation_all_angle_spinbox.setSingleStep(90)
        self.rotation_all_angle_spinbox.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        right_column.addWidget(self.rotation_all_angle_spinbox, alignment=Qt.AlignCenter)

        self.rotate_all_button = QPushButton("Rotacionar PDF Inteiro")
        self.rotate_all_button.clicked.connect(self.rotate_all_pages)
        self.rotate_all_button.setEnabled(False)
        right_column.addWidget(self.rotate_all_button, alignment=Qt.AlignCenter)

        right_column.addStretch()

        # Junta as duas colunas ao layout horizontal
        columns_layout.addLayout(left_column)
        columns_layout.addLayout(right_column)

        # Adiciona o layout horizontal ao layout principal
        main_layout.addLayout(columns_layout)

        # Define o layout principal na janela
        self.setLayout(main_layout)

        # Variáveis de controle
        self.folder_path = ""
        self.selected_pdf_path = ""
        self.selected_pdf_to_rotate_path = ""
        self.selected_pdf_to_rotate_all_path = ""

    def set_dark_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #2e2e2e; color: #f0f0f0; }
            QLineEdit, QSpinBox { background-color: #424242; color: #f0f0f0; }
            QPushButton { background-color: #555; color: white; padding: 5px; margin: 5px; }
            QPushButton:disabled { background-color: #333; }
            QCheckBox { color: #f0f0f0; }
        """)

    def set_light_theme(self):
        self.setStyleSheet("""
            QWidget { background-color: #f5f5dc; color: black; }
            QLineEdit, QSpinBox { background-color: white; color: black; }
            QPushButton { background-color: #f5f5dc; color: black; padding: 5px; margin: 5px; }
            QPushButton:disabled { background-color: #f5f5dc; }
            QCheckBox { color: black; }
        """)

    def toggle_theme(self, state):
        self.dark_mode = bool(state)
        if self.dark_mode:
            self.set_dark_theme()
        else:
            self.set_light_theme()

    # ==== Funções de seleção de arquivos ====

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Escolha uma pasta com PDFs")
        if folder:
            self.folder_path = folder
            self.label.setText(f"Pasta selecionada: {self.folder_path}")
            self.merge_button.setEnabled(True)
            self.select_pdf_button.setEnabled(True)
            self.select_rotate_pdf_button.setEnabled(True)
            self.select_rotate_all_pdf_button.setEnabled(True)

    def select_pdf(self):
        pdf_file, _ = QFileDialog.getOpenFileName(self, "Escolha um PDF", "", "PDF files (*.pdf)")
        if pdf_file:
            self.selected_pdf_path = pdf_file
            self.pdf_file_label.setText(os.path.basename(self.selected_pdf_path))
            self.split_button.setEnabled(True)

    def select_rotate_pdf(self):
        pdf_file, _ = QFileDialog.getOpenFileName(self, "Escolha um PDF", "", "PDF files (*.pdf)")
        if pdf_file:
            self.selected_pdf_to_rotate_path = pdf_file
            self.rotate_pdf_file_label.setText(os.path.basename(self.selected_pdf_to_rotate_path))
            self.rotate_button.setEnabled(True)

    def select_rotate_all_pdf(self):
        pdf_file, _ = QFileDialog.getOpenFileName(self, "Escolha um PDF", "", "PDF files (*.pdf)")
        if pdf_file:
            self.selected_pdf_to_rotate_all_path = pdf_file
            self.rotate_all_pdf_label.setText(os.path.basename(self.selected_pdf_to_rotate_all_path))
            self.rotate_all_button.setEnabled(True)

    # ==== Ações PDF ====

    def merge_pdfs(self):
        if not self.folder_path:
            QMessageBox.critical(self, "Erro", "Nenhuma pasta selecionada.")
            return

        merge_name = self.merge_name_entry.text().strip()
        if not merge_name:
            QMessageBox.critical(self, "Erro", "Insira um nome para o PDF unido.")
            return

        pdf_files = [f for f in os.listdir(self.folder_path) if f.endswith('.pdf')]
        if not pdf_files:
            QMessageBox.critical(self, "Erro", "Nenhum PDF encontrado na pasta.")
            return

        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(os.path.join(self.folder_path, pdf))

        output_path = os.path.join(self.folder_path, f"{merge_name}.pdf")
        merger.write(output_path)
        merger.close()
        QMessageBox.information(self, "Sucesso", "PDF unido criado com sucesso!")

    def split_pdf(self):
        if not self.selected_pdf_path:
            QMessageBox.critical(self, "Erro", "Nenhum PDF selecionado.")
            return

        start = self.start_page_spinbox.value() - 1
        end = self.end_page_spinbox.value()

        if start < 0 or end <= start:
            QMessageBox.critical(self, "Erro", "Intervalo de páginas inválido.")
            return

        reader = PdfReader(self.selected_pdf_path)
        writer = PdfWriter()

        for page in range(start, min(end, len(reader.pages))):
            writer.add_page(reader.pages[page])

        output_path = os.path.join(
            os.path.dirname(self.selected_pdf_path),
            f"dividido_{os.path.basename(self.selected_pdf_path)}"
        )
        with open(output_path, "wb") as f:
            writer.write(f)

        QMessageBox.information(self, "Sucesso", "PDF dividido com sucesso!")

    def rotate_pdf(self):
        if not self.selected_pdf_to_rotate_path:
            QMessageBox.critical(self, "Erro", "Nenhum PDF selecionado.")
            return

        page_index = self.page_to_rotate_spinbox.value() - 1
        angle = self.rotation_angle_spinbox.value()

        reader = PdfReader(self.selected_pdf_to_rotate_path)
        writer = PdfWriter()

        if page_index >= len(reader.pages):
            QMessageBox.critical(self, "Erro", "Número da página inválido.")
            return

        for i, page in enumerate(reader.pages):
            if i == page_index:
                page.rotate(angle)
            writer.add_page(page)

        output_path = os.path.join(
            os.path.dirname(self.selected_pdf_to_rotate_path),
            f"rotacionado_{os.path.basename(self.selected_pdf_to_rotate_path)}"
        )
        with open(output_path, "wb") as f:
            writer.write(f)

        QMessageBox.information(self, "Sucesso", "PDF rotacionado com sucesso!")

    def rotate_all_pages(self):
        if not self.selected_pdf_to_rotate_all_path:
            QMessageBox.critical(self, "Erro", "Nenhum PDF selecionado.")
            return

        angle = self.rotation_all_angle_spinbox.value()
        reader = PdfReader(self.selected_pdf_to_rotate_all_path)
        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(angle)
            writer.add_page(page)

        output_path = os.path.join(
            os.path.dirname(self.selected_pdf_to_rotate_all_path),
            f"rotacionado_todas_{os.path.basename(self.selected_pdf_to_rotate_all_path)}"
        )
        with open(output_path, "wb") as f:
            writer.write(f)

        QMessageBox.information(self, "Sucesso", "Todas as páginas foram rotacionadas!")


if __name__ == "__main__":
    app = QApplication([])
    window = PDFEditorApp()
    window.show()
    app.exec_()
