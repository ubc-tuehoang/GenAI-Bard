# GenAI-Bard

  * Install BARD AI on your Codespace instance:
  
  - From "main" branch:
   - click on the (green button) "<> CODE"
   - select "Codespaces" tab
   - click the + to launch Codespaces instance
      * This will launch a default Codespaces instance with 2-core 8GB RAM, 32GB (sufficient to build this image)
      * The browser navigates to the codespace instance: something like this... <some random name>gp.github.dev
  
   - At bottom, select tab "Terminal" - this is bash shell

     * Step 1: $>sudo apt update
     * Step 2: $>sudo apt upgrade
     * Step 3: To install Bard API:
        * $>pip install Bard
        * $>pip install bardapi

