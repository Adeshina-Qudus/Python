from Hacker_Rank import myCalculator


def mainMenu():
    menu = """
*************************
    *****^^^^****       *
    *    MENU   *       *
    *****^^^^****       *
*************************
1. * Phone book         *
2. * Messages           *
3. * Chat               *
4. * Call register      *
5. * Tones              *
6. * Setting            *
7. * Call divert        *
8. * Games              *
9. * Calculator         *
10.* Reminders          *
11.* Clock              *
12.* Profiles           *
13.* SIM services       *
*************************
            """
    print(menu)

    menu = int(input())
    match menu:
        case 1:
            phoneBook()
            return
        case 2:
            message()
            return
        case 3:
            chat()
            return
        case 4:
            callRegister()
            return
        case 5:
            tones()
            return
        case 6:
            settings()
            return
        case 7:
            callDivert()
            return
        case 8:
            games()
            return
        case 9:
            calculator()
            return
        case 10:
            reminders()
            return
        case 11:
            clock()
            return
        case 12:
            profiles()
            return
        case 13:
            SIM_services()


def phoneBook():
    phonebook = """
    
*************************
    *****^^^^****       *
    * PHONEBOOK *       *
    *****^^^^****       *
*************************
1. Search               *
2. Service Nos.         *
3. Add name             *
4. Erase                *
5. Edit                 *
6. Assign tone          *
7. Send b'card          *
8. Options              *
9. Speed dials          *
10.Voice tags           *
11. go back             *
*************************
                """
    print(phonebook)
    phonebook = int(input())
    match phonebook:
        case 1:
            print("Search")
            return
        case 2:
            print("Service Nos.")
            return
        case 3:
            print("Add name")
            return
        case 4:
            print("Erase")
            return
        case 5:
            print("Edit")
            return
        case 6:
            print("Assign tone")
            return
        case 7:
            print("Send b'card")
            return
        case 8:
            tov = """
*************************
    *****^^^^****       *
    *   OPTION  *       *
    *****^^^^****       *
*************************
1. Type of view         *
2. Memory status        *
3. go back              *
4. main menu            *
*************************
             """
            print(tov)
            tov = int(input())
            match tov:
                case 1:
                    print("Type of view")
                    return
                case 2:
                    print("Memory status")
                    return
                case 3:
                    phoneBook()
                case 4:
                    mainMenu()

        case 9:
            print("Speed dials")
            return
        case 10:
            print("Voice tags")
            return
        case 11:
            mainMenu()


def message():
    msg = """
*****************************
    *****^^^^****           *
    *  MESSAGE  *           *
    *****^^^^****           *
*****************************
1. * Write messages         *
2. * inbox                  *
3. * Outbox                 *
4. * Picture messages       *
5. * Templates              *   
6. * Smileys                *
7. * Message settings       *
8. * info service           *
9. * Voice mailbox number   *
10.* Services command editor*
11.* Go back                *
*****************************
"""
    print(msg)
    match msg:
        case 1:
            print("write messages")
            return
        case 2:
            print("inbox")
            return
        case 3:
            print("Outbox")
            return
        case 4:
            print("Picture messages")
            return
        case 5:
            print("Templates")
            return
        case 6:
            print("Smileys")
            return
        case 7:
            set1 = """
1. Set
2. Common 3
3. GO back
                     """
            print(set1)
            set1 = int(input())
            match set1:
                case 1:
                    msg1 = """
1. Message centre number
2. Messages sent as
3. Message validity
4. go back
5. main menu
                       """
                    print(msg1)
                    msg1 = int(input())
                    match msg1:
                        case 1:
                            print("Message centre number")
                        case 2:
                            print("Message sent as ")
                        case 3:
                            print("Message validity")
                        case 4:
                            message()
                        case 5:
                            mainMenu()
                case 2:
                    delivery = """
1. Delivery reports
2. Reply via same centre
3. Character support
4. go back
5. main menu
               """
                    print(delivery)
                    delivery = int(input())
                    match delivery:
                        case 1:
                            print("Delivery reports")

                        case 2:
                            print("Reply via same centre")
                        case 3:
                            print("Character support")
                        case 4:
                            message()
                        case 5:
                            mainMenu()
        case 8:
            print("Info service")
        case 9:
            print("Voice mailbox number")
        case 10:
            print("Service command editor")
        case 11:
            mainMenu()


def chat():
    cha = """
1. Chat
2. go back
          """
    print(cha)
    cha = int(input())
    match cha:
        case 1:
            print("Chat")
        case 2:
            mainMenu()


def callRegister():
    call = """
1. Missed calls      
2. Received calls
3. Dialled number 
4. Erase recent call list                
5. show call duration
6. Show call costs
7. Call cost settings 
8. Prepaid credit
                 """
    print(call)
    call = int(input())
    match call:
        case 1:
            print("""
1. DELIGHTED
   08072034442
2. AGNE
   07066221008
3. UDEME
   090182966447
                """)
        case 2:
            print("Received calls")
        case 3:
            print("Dialled number")
        case 4:
            print("Erase recent call list")
        case 5:
            lit = """
1. Last Call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
6. Go back
                    """
            print(lit)
            lit = int(input())
            match lit:
                case 1:
                    print("Last calls duration")
                case 2:
                    print("All calls' duration")
                case 3:
                    print("Received calls")
                case 4:
                    print("Dialled calls' duration")
                case 5:
                    print("Clear timers")
                case 6:
                    callRegister()

        case 6:
            las = """
1. Last call cost
2. All calls' cost
3. Clear counters
4. Go bck
                  """
            print(las)
            match las:
                case 1:
                    print("Last call cost")
                case 2:
                    print("All calls' cost")
                case 3:
                    print("Clear counters")
                case 4:
                    callRegister()

        case 7:
            call = """
1. Call cost limit
2. Show costs in
3. Go back
                    """
            print(call)
            call = int(input())
            match call:
                case 1:
                    print("Call cost limit")
                case 2:
                    print("Sow costs in")
                case 3:
                    callRegister()

        case 8:
            print("Prepaid credit")


def tones():
    tone = """
*************************
    *****^^^^****       *
    *   TONES   *       *
    *****^^^^****       *
*************************    
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9 Screen saver
10.Go back
                        """
    print(tone)
    tone = int(input())
    match tone:
        case 1:
            print("Ringing tone")
        case 2:
            print("Ringing volume")
        case 3:
            print("Incoming call alert")
        case 4:
            print("Composer")
        case 5:
            print("Message alert tone")
        case 6:
            print("Keypad tone")
        case 7:
            print("Warning and game tones")
        case 8:
            print("Vibrating alert")
        case 9:
            print("Screen saver")
        case 10:
            tones()


def settings():
    sett = """
1. Call settings
2. Phone settings
3. Security setting  
4. Restore factory settings
                        """
    print(sett)
    sett = int(input())
    match sett:
        case 1:
            auto = """
1. Automatic redial
2. Speed dialing
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
7. Go back
                                        """
            print(auto)
            auto = int(input())
            match auto:
                case 1:
                    print("Automatic redial")
                case 2:
                    print("Speed dialing")
                case 3:
                    print("Call waiting options")
                case 4:
                    print("Own number sending")
                case 5:
                    print("Phone line in use")
                case 6:
                    print("Automatic answer")
                case 7:
                    settings()
        case 2:
            lang = """
*************************
    *****^^^^****       *
    *  LANGUAGE *       *
    *****^^^^****       *
*************************            
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm SIM service action
7. Go back
                        """
            print(lang)
            lang = int(input())
            match lang:
                case 1:
                    print("Language")
                case 2:
                    print("Call info display")
                case 3:
                    print("Welcome note")
                case 4:
                    print("Network selection")
                case 5:
                    print("Lights")
                case 6:
                    print("Confirm SIM service action")
                case 7:
                    settings()

        case 3:
            pin = """
1. PIN code request
2. Call barring service
3. Fixed dilling
4. Closed user group
5. Phone security
6. Change access codes
7. Go back
                """
            print(pin)
            pin = int(input())
            match pin:
                case 1:
                    print("PIN code request")
                case 2:
                    print("Call barring service")
                case 3:
                    print("Fixed dilling")
                case 4:
                    print("Closed user group")
                case 5:
                    print("Phone security")
                case 6:
                    print("Change access codes")
                case 7:
                    settings()

        case 4:
            print("Restore factory settings")


def callDivert():
    call = """
1.Call divert
2. Go back
                 """
    print(call)
    call = int(input())
    match call:
        case 1:
            print("call divert")
        case 2:
            callDivert()


def games():
    game = """
                 1.Games
                 2.Go back
                        """
    print(game)
    game = int(input())
    match game:
        case 1:
            print("Games")
        case 2:
            games()


def calculator():
    cal = """
1.calculator
2.Go back
                    """
    print(cal)
    cal = int(input())
    match cal:
        case 1:
            add = """
1.ADDITION
2.SUBTRACTION
3.MULTIPLY 
4.DIVIDE
5.SQUARE 
            """
            print(add)
            add = int(input())
            match add:
                case 1:
                    num = int(input("Enter Number "), myCalculator.addNumbers())
                    print(num)
                    return
                case 2:
                    myCalculator.subtractNumber()
                    return
                case 3:
                    myCalculator.maximum()
                    return

        case 2:
            calculator()


def reminders():
    remind = """
1.Reminder
2.Go back
                """
    print(remind)
    remind = int(input())
    match remind:
        case 1:
            print("Reminder")
            return
        case 2:
            reminders()


def clock():
    cloc = """
*************************
    *****^^^^****       *
    *   CLOCK   *       *
    *****^^^^****       *
*************************
1. Alarm clock
2. Clock setting
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
7.Go back
"""
    print(cloc)
    cloc = int(input())
    match cloc:
        case 1:
            print("Alarm clock")
            return
        case 2:
            print("Clock settings")
            return
        case 3:
            print("Date settings")
            return
        case 4:
            print("Stopwatch")
            return
        case 5:
            print("Countdown timer")
            return
        case 6:
            print("Auto update of date and time")
            return
        case 7:
            clock()


def profiles():
    pro = """
1. profiles
2. Go back
                    """
    print(pro)
    pro = int(input())
    match pro:
        case 1:
            print("profiles")
            return
        case 2:
            mainMenu()


def SIM_services():
    sim = """
1. Sim services
2. Go back
                """
    print(sim)
    sim = int(input())
    match sim:
        case 1:
            print("Sim services")
            return
        case 2:
            phoneBook()
