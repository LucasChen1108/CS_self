-- Keep a log of any SQL queries you execute as you solve the mystery.
--Get the tables' name
.table
/*
airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers
*/


-- Look through the records on July 28th
SELECT * FROM crime_scene_reports WHERE month = 7 AND day = 28;
/*
| 295 | 2024 | 7     | 28  | Humphrey Street
| Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery. |
*/

--According to the records from the crime reports, 3 witnesses were interviewd on the same day, and they all mentioned the word 'bakery', so I check what they have said.
SELECT * FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';
/*
| 161 | Ruth    | 2024 | 7     | 28
| Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
                                                          |
| 162 | Eugene  | 2024 | 7     | 28
| I don't know the thief's name, but it was someone I recognized.
Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
                                                                                            |
| 163 | Raymond | 2024 | 7     | 28
| As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket. |
*/


--According to Ruth, 10:15 a.m.(+10 minutes), thief leave the parking lot in car, so checked the record from the
SELECT * FROM bakery_security_logs
WHERE month = 7 AND day = 28
AND hour = 10
AND minute >= 15 AND minute <= 25 ;
/*
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 260 | 2024 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2024 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2024 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2024 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2024 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2024 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2024 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2024 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
+-----+------+-------+-----+------+--------+----------+---------------+
*/


--According to Eugene, In the morning before 10:15 a.m. that day, thief withdrew some money from the ATM on Leggett Street. So I should check who has withdrown money in that period.
SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
/*
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2024 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2024 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2024 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2024 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2024 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 275 | 86363979       | 2024 | 7     | 28  | Leggett Street | deposit          | 10     |
| 288 | 25506511       | 2024 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2024 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2024 | 7     | 28  | Leggett Street | withdraw         | 35     |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
*/

-- Use the account_number to get the list of possible options of the thief
SELECT * FROM people WHERE id IN (
    SELECT person_id FROM bank_accounts WHERE account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
    )
);
/*
+--------+---------+----------------+-----------------+---------------+
|   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       |
| 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
| 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
| 948985 | Kaelyn  | (098) 555-1164 | 8304650265      | I449449       |
+--------+---------+----------------+-----------------+---------------+
*/

-- Use the license_plate from the bakery car park to futher narrow down the range.
SELECT * FROM people WHERE id IN (
    SELECT person_id FROM bank_accounts WHERE account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE month = 7 AND day = 28
        AND atm_location = 'Leggett Street'
    )
)
AND license_plate IN (
    SELECT license_plate FROM bakery_security_logs
    WHERE month = 7 AND day = 28
    AND hour = 10
    AND minute >= 15 AND minute <= 25
);
/*
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
*/

--According to Raymond, thief is going to tame the earliest flight on July 29th. Phone call records can be checked arount the tame, the duration is less than a minute. Also noticed the people on the other side is the accompliance.
-- Let's Check the phone call first, find out the caller that is in the suspecious list and also meet the description. We successfully narrow down the list to two people.
SELECT * FROM people WHERE phone_number IN(
    SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60
    AND caller IN (
        SELECT phone_number FROM people WHERE id IN (
            SELECT person_id FROM bank_accounts WHERE account_number IN (
                SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28
                AND atm_location = 'Leggett Street'
            )
        )
        AND license_plate IN (
            SELECT license_plate FROM bakery_security_logs
            WHERE month = 7 AND day = 28
            AND hour = 10
            AND minute >= 15 AND minute <= 25
        )
    )
);

SELECT * FROM people WHERE phone_number IN(
    SELECT receiver FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60
    AND caller IN (
        SELECT phone_number FROM people WHERE id IN (
            SELECT person_id FROM bank_accounts WHERE account_number IN (
                SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28
                AND atm_location = 'Leggett Street'
            )
        )
        AND license_plate IN (
            SELECT license_plate FROM bakery_security_logs
            WHERE month = 7 AND day = 28
            AND hour = 10
            AND minute >= 15 AND minute <= 25
        )
    )
);
/*
+-----+----------------+----------------+------+-------+-----+----------+
| id  |     caller     |    receiver    | year | month | day | duration |
+-----+----------------+----------------+------+-------+-----+----------+
| 233 | (367) 555-5533 | (375) 555-8161 | 2024 | 7     | 28  | 45       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2024 | 7     | 28  | 49       |
+-----+----------------+----------------+------+-------+-----+----------+
Possible thief:
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
Possible accompliance
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 847116 | Philip | (725) 555-3243 | 3391710505      | GW362R6       |
| 864400 | Robin  | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+--------+----------------+-----------------+---------------+
*/

--Finally let's check the flight
--First find the earliest flight on July 29th
SELECT * FROM flights WHERE
month = 7 AND day = 29
AND origin_airport_id = (
    SELECT id FROM airports
    WHERE city = 'Fiftyville'
)
ORDER BY hour ASC, minute ASC
LIMIT 1;
/*
+----+-------------------+------------------------+------+-------+-----+------+--------+
| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
+----+-------------------+------------------------+------+-------+-----+------+--------+
| 36 | 8                 | 4                      | 2024 | 7     | 29  | 8    | 20     |
+----+-------------------+------------------------+------+-------+-----+------+--------+
*/

-- We then can find there destination
SELECT * FROM airports WHERE id IN(
    SELECT destination_airport_id FROM flights WHERE
    month = 7 AND day = 29
    AND origin_airport_id = (
        SELECT id FROM airports
        WHERE city = 'Fiftyville'
    )
    ORDER BY hour ASC, minute ASC
    LIMIT 1
);
/*
+----+--------------+-------------------+---------------+
| id | abbreviation |     full_name     |     city      |
+----+--------------+-------------------+---------------+
| 4  | LGA          | LaGuardia Airport | New York City |
+----+--------------+-------------------+---------------+
*/

-- We are coming to the end ! Siuuuuu~
SELECT * FROM people WHERE passport_number = (
    SELECT passport_number FROM passengers WHERE flight_id = (
        SELECT id FROM flights WHERE
        month = 7 AND day = 29
        AND origin_airport_id = (
            SELECT id FROM airports
            WHERE city = 'Fiftyville'
        )
        ORDER BY hour ASC, minute ASC
        LIMIT 1
    )
    AND passport_number IN (
        SELECT passport_number FROM people WHERE phone_number IN(
            SELECT caller FROM phone_calls
            WHERE month = 7 AND day = 28 AND duration < 60
            AND caller IN (
                SELECT phone_number FROM people WHERE id IN (
                    SELECT person_id FROM bank_accounts WHERE account_number IN (
                        SELECT account_number FROM atm_transactions
                        WHERE month = 7 AND day = 28
                        AND atm_location = 'Leggett Street'
                    )
                )
                AND license_plate IN (
                    SELECT license_plate FROM bakery_security_logs
                    WHERE month = 7 AND day = 28
                    AND hour = 10
                    AND minute >= 15 AND minute <= 25
                )
            )
        )
    )
);
/*
The THIEF !!!!!!!
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+-------+----------------+-----------------+---------------+
*/


SELECT * FROM people WHERE phone_number IN(
    SELECT receiver FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60
    AND caller IN (
        SELECT phone_number FROM people WHERE id IN (
            SELECT person_id FROM bank_accounts WHERE account_number IN (
                SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28
                AND atm_location = 'Leggett Street'
            )
        )
        AND license_plate IN (
            SELECT license_plate FROM bakery_security_logs
            WHERE month = 7 AND day = 28
            AND hour = 10
            AND minute >= 15 AND minute <= 25
        )
    )
    AND caller = (
        SELECT phone_number FROM people WHERE passport_number = (
            SELECT passport_number FROM passengers WHERE flight_id = (
                SELECT id FROM flights WHERE
                month = 7 AND day = 29
                AND origin_airport_id = (
                    SELECT id FROM airports
                    WHERE city = 'Fiftyville'
                )
                ORDER BY hour ASC, minute ASC
                LIMIT 1
            )
            AND passport_number IN (
                SELECT passport_number FROM people WHERE phone_number IN(
                    SELECT caller FROM phone_calls
                    WHERE month = 7 AND day = 28 AND duration < 60
                    AND caller IN (
                        SELECT phone_number FROM people WHERE id IN (
                            SELECT person_id FROM bank_accounts WHERE account_number IN (
                                SELECT account_number FROM atm_transactions
                                WHERE month = 7 AND day = 28
                                AND atm_location = 'Leggett Street'
                            )
                        )
                        AND license_plate IN (
                            SELECT license_plate FROM bakery_security_logs
                            WHERE month = 7 AND day = 28
                            AND hour = 10
                            AND minute >= 15 AND minute <= 25
                        )
                    )
                )
            )
        )
    )
);
/*
The accomplice is YOU !!!!
+--------+-------+----------------+-----------------+---------------+
|   id   | name  |  phone_number  | passport_number | license_plate |
+--------+-------+----------------+-----------------+---------------+
| 864400 | Robin | (375) 555-8161 | NULL            | 4V16VO0       |
+--------+-------+----------------+-----------------+---------------+
*/


/*
Successfully solved !!!!
The THIEF is: Bruce
The city the thief ESCAPED TO: New York City
The ACCOMPLICE is: Robin
*/
