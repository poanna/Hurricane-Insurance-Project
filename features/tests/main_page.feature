Feature: test cases for hurricane insurance page

    Scenario: User can see required when leave the zip code 
        Given Open the main page
        When Click on Get a Quote button
        Then User can see Required message

    Scenario: User can see invalid zip code message when enter invalid zip code
        Given Open the main page
        When Enter 1234 in zip code field
        And Click on Get a Quote button
        Then User can see Invalid zip code message

    Scenario: User can enter a valid zip code and select bricks on building materials
        Given Open the main page
        When Enter 90210 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        Then Verify water-proximity page opened

    Scenario: User can submit water proximity option
        Given Open the main page
        When Enter 80926 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        And Select yes on Water Proximity question
        And Click on Next button
        Then Verify quote page opened

    Scenario: User can see Included Flood Protection label
        Given Open the main page
        When Enter 90210 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        And Select yes on Water Proximity question
        And Click on Next button
        Then Verify quote page opened
        And Verify Include Flood Protection label

    Scenario: User find the checkbox unmarked on the quote page
        Given Open the main page
        When Enter 90211 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        And Select yes on Water Proximity question
        And Click on Next button
        Then Verify quote page opened
        And Verify checkbox is unmarked

    Scenario: User can see two plan options
        Given Open the main page
        When Enter 11223 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        And Select yes on Water Proximity question
        And Click on Next button
        Then Verify quote page opened
        And Verify two plan options

    Scenario: User can click on plan options
        Given Open the main page
        When Enter 11223 in zip code field
        And Click on Get a Quote button
        And Select Bricks on Building Materials
        And Click on Next button
        And Select yes on Water Proximity question
        And Click on Next button
        Then Verify quote page opened
        And Verify plan options are clickable
