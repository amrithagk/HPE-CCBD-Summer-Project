Feature: Searching for Sony TV reviews on Amazon

  Scenario: User wants to find reviews of a Sony TV on Amazon
    Given the user is on the Amazon homepage
    When the user searches for "Sony TV"
    And the user clicks on the 3rd search result
    And the user navigates to the reviews section
    Then the user should be able to view the reviews

