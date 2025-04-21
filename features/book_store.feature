Feature: Book Store Application testing

  Background:
    Given the user has launched the DEMOQA application
    And the user click on "Book Store Application" card
    Then the user should be navigated to a URL containing "demoqa.com/books"
    Then the menu list for "Book Store Application" should be expanded
    Then the menu list items for "Book Store Application" should be
      |Items                |
      |Login                |
      | Book Store          |
      | Profile             |
      | Book Store API      |

  Scenario: Look at the list of books and use the api to validate the correctness of the data displayed on the book store page
    Then the user navigates to "Book Store" section under "Book Store Application"
    And the user selects "5" in the row per page dropdown
    And the user fetches the books details displayed
    And check if Book Store API is available
    And send a GET request to endpoint "/BookStore/v1/Books" and fetch response
    And parse the book details from the response
    Then compare the books details displayed with the book details fetched through API

