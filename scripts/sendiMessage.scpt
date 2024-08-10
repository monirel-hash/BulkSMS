on run {targetPhone, message}
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy targetPhone of targetService
        send message to targetBuddy
    end tell
end run