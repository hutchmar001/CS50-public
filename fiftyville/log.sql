-- Keep a log of any SQL queries you execute as you solve the mystery.
// The theft took place on July 28, 2021 on Humphrey Street.

SELECT * FROM crime_scene_reports
WHERE street = "Humphrey Street" AND day = "28";

// Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
Interviews were conducted today with three witnesses who were present at the time -
each of their interview transcripts mentions the bakery.

SELECT * FROM interviews
WHERE month = "7" AND day = "28";

// | 161 | Ruth  Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
| 162 | Eugene  I don't know the thief's name, but it was someone I recognized.
Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
| 163 | Raymond   As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket. |

SELECT * FROM flights
WHERE month = "7" AND day = "29";

// id = 36, origin_airport_id = 8, destination_airport_id = 4, 8:20

SELECT * FROM airports;

// Flight was from Fiftyville to LaGuardia Airport in New York City.

SELECT * FROM bakery_security_logs
WHERE month = "7" AND day = "28" AND hour = "10" AND minute <= "25";

SELECT * FROM people
WHERE license_plate = "5P2BI95" OR license_plate = "94KL13X" OR license_plate = "6P58WS2" OR license_plate = "4328GD8" OR licens
e_plate = "G412CB7" OR license_plate = "L93JTIZ" OR license_plate = "322W7JE" OR license_plate = "0NTHK55";

// Suspects and their info:

   id   |  name   |  phone_number  | passport_number | license_plate |
+--------+---------+----------------+-----------------+---------------+
| 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
| 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
| 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
| 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
| 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
| 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
| 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
| 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |

SELECT * FROM phone_calls WHERE month = "7" AND day = "28" AND duration < "60";

// Narrowed down to:
Sofia called (996) 555-8899
Kelsey called (892) 555-8872 and (717) 555-1342
Bruce called (375) 555-8161
Diana called (725) 555-3243








