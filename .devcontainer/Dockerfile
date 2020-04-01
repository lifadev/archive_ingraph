FROM python:3.8-buster

RUN set -ex; \
    \
    echo "deb https://deb.nodesource.com/node_13.x buster main" \
        > /etc/apt/sources.list.d/node.list; \
    wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -; \
    \
    apt update; \
    apt install --yes --no-install-recommends \
        git make nodejs silversearcher-ag tree zip; \
    \
    pip install poetry; \
    mkdir -p ~/.config/pypoetry; \
    echo '[virtualenvs]\ncreate=false' > ~/.config/pypoetry/config.toml; \
    \
    echo 'export PS1="\w>>> "' > ~/.bashrc

CMD ["/bin/bash"]
