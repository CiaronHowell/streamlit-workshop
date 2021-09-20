mkdir -p ~/.streamlit/
printf "[server]\nheadless=true\nenableCORS=false\n" "${PORT}" > ~/.streamlit/config.toml