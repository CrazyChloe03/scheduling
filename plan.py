def code():
  import os
  events = []
  f = open("events.txt", "w")
  def write_file(event, name, date, time, description):
    f = open("events.txt","a")
    f.write(f"{event['name']} on {event['date']} at {event['time']} ({event['description']})\n")
    f.close()

  def user_input():
    os.system("clear")
    name = input("Enter event name: ")
    date = input("Enter event date: ")
    time = input("Enter event time: ")
    description = input("Enter event description: ")
    add_event(name, date, time, description)

  def print_events():
    with open("events.txt", "r") as file:
      print(file.read())

  def add_event(name, date, time, description):
    event = {
        'name': name,
        'date': date,
        'time': time,
        'description': description
    }
    write_file(event, name, date, time, description)
    events.append(event)
    os.system("clear")
    print(f"Event {name} added successfully")

  def display_upcoming_events():
    if not events:
      os.system("clear")
      print("No upcoming events")
    else:
      os.system('clear')
      print_events()

  def edit_event():
    edit_name = input("Enter event name to edit: ")
    for event in events:
      if event['name'] == edit_name:
        os.system("clear")
        print(f"Editing {event['name']} press enter to keep")
        edit_name = input("Enter new event name: ")
        if edit_name != "":
          event['name'] = edit_name
        edit_date = input("Enter new date: ")
        if edit_date != "":
          event['date'] = edit_date
        edit_time = input("Enter new time: ")
        if edit_time != "":
          event['time'] = edit_time
        edit_description = input("Enter new description: ")
        if edit_description != "":
          event['description'] = edit_description
        os.system("clear")
        print(f"Event {event['name']} edited successfully")
          
      for event in events:
          if event['name'] == name:
              event['name'] = name
              event['date'] = date
              event['time'] = time
              event['description'] = description
              with open("events.txt", "r") as file:
                  data = file.readlines()
              with open("events.txt", "w") as file:
                  for line in data:
                      if event['name'] in line:
                          file.write(f"{event['name']} on {event['date']} at {event['time']} ({event['description']})\n")
                      else:
                          file.write(line)
              print(f"Event {name} edited successfully")
              break
      else:
        os.system("clear")
        print(f"Event {edit_name} not found")

  while True:
    print("\n\nPersonal Event Planner")
    print("1. Add new event")
    print("2. View upcoming events")
    print("3. Edit event")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
      user_input()

    elif choice == '2':
      display_upcoming_events()

    elif choice == '3':
      edit_event()

    elif choice == '4':
      os.system('clear')
      print("Thanks for using")
      break

    else:
      os.system('clear')
      print("Please enter 1/2/3/4")
code()
