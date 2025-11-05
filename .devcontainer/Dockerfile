FROM python:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget git \
    poppler-utils \
    tesseract-ocr \
    libxml2-dev \
    libxslt-dev && \
    sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.2.1/zsh-in-docker.sh)" -- \
        -p git \
        -p https://github.com/zsh-users/zsh-autosuggestions \
        -p https://github.com/zsh-users/zsh-syntax-highlighting \
        -a 'export TERM=xterm-256color' && \
    echo 'DISABLE_AUTO_UPDATE=true' >> ~/.zshrc && \
    echo 'DISABLE_UPDATE_PROMPT=true' >> ~/.zshrc && \
    echo 'export HISTFILE=/home/vscode/.zsh_history' >> ~/.zshrc && \
    echo '[[ -f /home/vscode/.p10k.zsh ]] && source /home/vscode/.p10k.zsh' >> ~/.zshrc

WORKDIR /workspaces/automl-tsv-builder

COPY .devcontainer/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
