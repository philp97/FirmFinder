Get a list of firms and determine if they are state ownedor private and their area of operation.

## Firm Classification and Business Line Detection Using Crewai 

This project leverages the power of Crewai to automate the classification of firms based on ownership status (state-owned or private) and to identify their main line of business. The application takes a list of firm names, searches for relevant information online, and returns structured data regarding each firm's ownership type and primary industry.

Features
Automated Firm Classification: Determine whether a firm is state-owned or private based on online data.
Business Line Identification: Extract and classify the main line of business for each firm.
Scalable: Can process large lists of firms efficiently.
Customizable: Modify search parameters and classification criteria based on specific needs.
Prerequisites
Crewai API Key: Ensure you have an active Crewai API key.
Python 3.x: The application is built using Python.
Required Libraries: Install the necessary Python packages using pip install -r requirements.txt.
Installation
Clone the repository:

# Firm Classification and Business Line Detection Using Crewai

This project leverages the power of Crewai to automate the classification of firms based on ownership status (state-owned or private) and to identify their main line of business. The application takes a list of firm names, searches for relevant information online, and returns structured data regarding each firm's ownership type and primary industry.

## Features

- **Automated Firm Classification:** Determine whether a firm is state-owned or private based on online data.
- **Business Line Identification:** Extract and classify the main line of business for each firm.
- **Scalable:** Can process large lists of firms efficiently.
- **Customizable:** Modify search parameters and classification criteria based on specific needs.

## Prerequisites

- **Crewai API Key:** Ensure you have an active Crewai API key.
- **Python 3.x:** The application is built using Python.
- **Required Libraries:** Install the necessary Python packages using `pip install -r requirements.txt`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/firm-classification.git
   cd Firmfinder
   
2. Run the model
   
    ```bash
    poetry install --no-root
    poetry shell
    python main.py

3. Enter firms names   

   ```bash
    ## Welcome to Crew AI Template
   -------------------------------
   Enter List of Firms: Tesla, Banco do Brasil, Vale S.A., Petrobras

4. Output 

   ```bash
   ########################
   ## Here is you custom crew run result:
   ########################
   Tesla, Private, Technology
   Banco do Brasil, State, Bank
   Vale S.A., Private, Mining and Energy
   Petrobras, State, Oil and Gas

  
   










