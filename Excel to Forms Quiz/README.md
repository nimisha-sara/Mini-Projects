# Quiz Maker (Google Forms API)

Convert an Excel of the given format to a google forms quiz. 

| Question                           | Option 1    | Option 2    | Option 3    | Option 4    | Correct Answer |
|-----------------------------------|-------------|-------------|-------------|-------------|----------------|
|                                   |             |             |             |             |                |


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/nimisha-sara/Mini-Projects.git
    ```
2. Go to project directory

3. Install python libraries
   ```sh
   pip install -r requirements.txt
   ```
4. Get OAuth client ID (`client_secret.json`) from google console after enabling forms API. [reference](https://developers.google.com/forms/api/quickstart/python). 
   
5. Run the function `create_google_form_from_excel` with parameters 
    ```
    excel_file: location of file
    num_rows: no of rows of excel, to be made into quiz
    ``` 
    from main.py file
