Feature: Dynamic Property testing

  Background:
    Given the user has launched the DEMOQA application
    And the user click on "Elements" card
    Then the user should be navigated to a URL containing "demoqa.com/elements"
    Then the menu list for "Elements" should be expanded
    Then the menu list items for "Elements" should be
      |Items               |
      |Text Box             |
      | Check Box              |
      | Radio Button           |
      | Web Tables             |
      | Buttons                |
      | Links                  |
      | Broken Links - Images  |
      | Upload and Download    |
      | Dynamic Properties     |
    Then the user navigates to "Dynamic Properties" section under "Elements"
    Then the user should be navigated to a URL containing "demoqa.com/dynamic-properties"

    Scenario: Fluently wait for button with text “Visible after 5 seconds” to be displayed (TC003)
      Then the user fluently waits for the button with text "Visible after 5 seconds" to be displayed

    Scenario: Load the page and verify that the second button changes color after some time (TC004)
      Given the user fetches initial "color" of the button from css property
      And the user polls to wait until the button color changes
      And the user fetches changed "color" of the button from css property
      Then the user asserts if the color of the button has changed

