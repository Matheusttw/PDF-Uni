# PDF Uni 🚀

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Uma ferramenta de desktop simples e poderosa, construída em Python com PyQt5, para simplificar tarefas comuns de manipulação de PDFs. Ideal para profissionais de dados, desenvolvedores e qualquer pessoa que lida com documentos digitais frequentemente.

### Visão Geral

O **PDF Uni** oferece uma interface gráfica intuitiva para Unir, Dividir e Rotacionar arquivos PDF com apenas alguns cliques, eliminando a necessidade de ferramentas online ou software caro.

---

### ✨ Relevância para Profissionais de Dados e Desenvolvedores

No universo de **Ciência de Dados, Análise de Dados e Engenharia de Dados**, lidamos constantemente com relatórios, artigos e datasets em formato PDF. Esta ferramenta foi pensada para otimizar o fluxo de trabalho:

* **Pré-processamento de Dados:** Muitos relatórios digitalizados ou mal exportados chegam com páginas rotacionadas. A função de rotação é essencial para corrigir a orientação antes de aplicar técnicas de OCR (Reconhecimento Óptico de Caracteres) para extração de texto e tabelas.
* **Gestão de Relatórios:** Unifique múltiplos relatórios semanais ou mensais em um único documento para análise consolidada.
* **Extração de Informação:** Divida grandes manuais ou documentos extensos para isolar apenas as seções relevantes (capítulos, apêndices) que contêm os dados que você precisa analisar.
* **Automação:** Embora seja uma ferramenta GUI, o código subjacente serve como um excelente exemplo de como utilizar a biblioteca `PyPDF2` para automatizar essas tarefas em scripts de ETL (Extração, Transformação e Carga) ou pipelines de dados.

---

### 🔧 Funcionalidades Principais

O aplicativo é dividido em seções claras para uma experiência de usuário eficiente:

1.  **Unir PDFs:**
    * Selecione uma pasta e o **PDF Uni** irá mesclar todos os arquivos `.pdf` contidos nela em um único documento.
    * Personalize o nome do arquivo de saída.

2.  **Dividir PDF:**
    * Escolha um arquivo PDF específico.
    * Defina o intervalo de páginas (inicial e final) que deseja extrair.
    * Gere um novo PDF contendo apenas as páginas selecionadas.

3.  **Rotacionar PDF:**
    * **Página Específica:** Rotacione uma única página dentro de um documento (90°, 180° ou 270°).
    * **Documento Inteiro:** Aplique uma rotação a todas as páginas do PDF de uma só vez.

4.  **Interface Moderna:**
    * Inclui um tema claro e um tema escuro (`Skin Dark`) para maior conforto visual.
  
<img width="333" height="477" alt="skinbeg" src="https://github.com/user-attachments/assets/a16f8c50-4a5b-4801-a0a6-ddf23936bbd4" />
<img width="334" height="478" alt="pdf uni" src="https://github.com/user-attachments/assets/3c11a439-bb49-4146-841d-ba3e6644de56" />


---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Interface Gráfica (GUI):** PyQt5
* **Manipulação de PDF:** PyPDF2

---

### ⚙️ Instalação e Execução

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Matheusttw/PDF-uni.git](https://github.com/seu-usuario/pdf-uni.git)
    cd pdf-uni
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python pdfuni2.1.py
    ```

---

###  CONTRIBUTING

Contribuições são sempre bem-vindas! Se você tem ideias para novas funcionalidades, melhorias na interface ou correções de bugs, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

---

### 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
