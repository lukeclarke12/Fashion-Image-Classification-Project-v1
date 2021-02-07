mkdir -p ~/.streamlit/
echo"\
[general]\n\
email = \"luke.clarke@bts.tech\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
