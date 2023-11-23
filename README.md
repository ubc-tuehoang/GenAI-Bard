# GenAI-Bard AI Chat

  * Install BARD AI on your Codespace instance:
  
  - From "main" branch:
   - click on the (green button) "<> CODE"
   - select "Codespaces" tab
   - click the + to launch Codespaces instance
      * This will launch a default Codespaces instance with 2-core 8GB RAM, 32GB (sufficient to build this)
      * The browser navigates to the codespace instance: something like this... <some random name>gp.github.dev
  
   - At bottom, select tab "Terminal" - this is bash shell

     * Step 1: $>sudo apt update
     * Step 2: $>sudo apt upgrade
     * Step 3: To install Bard API:
        * $>pip install Bard
        * $>pip install bardapi

   * How to extract ##Secure-PSID## token
      * Requirement: (for Canada) VPN connection to host outside of Canada.
      * Open browser to BardAI (https://bard.google.com)
      * View source to search for PSID
      * Copy PSID and use in the code for token='[PSID from browser]'


  * Execute python code:
      * $>python ./bard-api.py

