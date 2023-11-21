raw_string_stops = input()
command = input()

while command != "Travel":
    command_type, index_or_old_string, end_index_or_string = [int(x) if x.isdigit() else x for x in command.split(":")]
    if "Switch" in command_type and index_or_old_string in raw_string_stops:
        raw_string_stops = raw_string_stops.replace(index_or_old_string, end_index_or_string)
    elif "Add Stop" in command_type and 0 <= index_or_old_string < len(raw_string_stops):
        raw_string_stops = f"{raw_string_stops[:index_or_old_string]}{end_index_or_string}{raw_string_stops[index_or_old_string:]}"
    elif "Remove Stop" in command_type and 0 <= index_or_old_string < len(
            raw_string_stops) and 0 <= end_index_or_string < len(raw_string_stops):
        raw_string_stops = f"{raw_string_stops[:index_or_old_string]}{raw_string_stops[end_index_or_string + 1:]}"
    print(raw_string_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {raw_string_stops}")
