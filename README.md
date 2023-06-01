# sdet-automation-test
## What is Expected?
This is a code challenge to test your skills related to the development of automated tests. There are two scenarios, on
for frontend, testing a webpage, and another to test some API calls.
For the first, it's required to do it using Java. For the second, it's required to do it using Python.

## Test Scenario - Front End test [JAVA]
This test consists in some steps to interact with a web page and assert some conditions, generating a report with the test result after the execution.

For this test you should follow the steps:
1. Go to https://www.amazon.com and expand the 'All' hamburger menu

![](./imgs/img_1.jpg)
2. Under 'Shop By Department' open 'Arts & Craft'

![](./imgs/img_2.jpg)
3. Open 'Beading & Jewelry Making'

![](./imgs/img_3.jpg)
4. Open 'Engraving Machines & Tools'

![](./imgs/img_4.jpg)
5. Sort by Price: High to Low

![](./imgs/img_5.jpg)
6. For the products that are currently available, open the third one.
7. Check the review score. If it's less than 4, fail the test, otherwise pass it.
8. Check the price for the opened item. If it's more than $4000, fail the test, otherwise pass it.
9. Generate a report with the test result. In case of failure, attach a screenshot of the current page in the report.

## Second Scenario - API [Python]
NASA has an open API: https://api.nasa.gov/index.html#getting-started. Test the following scenarios
1. Query the Astronomy Picture of the Day with 5 images. See if the return has 5 entries in it.
2. Query the Astronomy Picture of the Day from 2022-05-05 to 2022-05-20. See if the return has 16 entries in it.
3. Create some integration scenarios to test edge, valid, and invalid scenarios for the Astronomy Picture of the Day API

## Repository
You will need to fork the repository and build the solution in Github publicly. Once you are finished, share your
repository with us. We expect this to be finished in one week, but if anything happens and this deadline cannot be met, 
reach out, so we know what is happening instead of think that you are not interested in this position anymore. 

## Deliverables:
* Code in a public Github repository
* README file with the notes, documentation, and instructions related to the code developed
* The test execution should do the above steps and generate a report with the tests results. In case of a test failure, it should also attach a screenshot of the current page when the test failed.
