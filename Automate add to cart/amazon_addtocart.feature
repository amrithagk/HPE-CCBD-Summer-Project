Feature: Login to Amazon e commerce and product purchase

  Scenario Outline: Get price, description, and offers for a specific TV
  
    Given I launch Chrome browser
    When I visit amazon website
    And Amazon homepage is opened successfully
  
    And I log in with valid phone number or email "<mobileno>" and password "<password>"
    And I should login successfully with "<username>"
  
    #And search for the "<product>"
    #And click on search button

    #Then find the third product
    #And fetch price of the product
    #And fetch the description of product
    #And click add to cart button
  
    #And Displays the offers
      
    #And the user navigates to the reviews section
    #And the user should be able to view the reviews

    #And send email notification

    Examples:
      |mobileno|password|username|product|
      #|9387823787|xyz|name|Sony 55inch TV|
       |7019522431|abcd|Nisarga|Sony 55inch TV|
      #|7019522431|Nisarga@123|name|Sony 55inch TV|
      #|7019522431|Nisarga@123|Nisarga|rfghbghkjrf|
      #|7019522431|Nisarga@123|Nisarga|Sony 55inch TV|
  
