-- Copyright (c) 2012 Objective Development
-- http://www.obdev.at/
-- Version 1

on run argv
	set nr to item 1 of argv
	set news to ""
	if nr = "0" then
		set news_title to "Nothing Added!"
	else
		if nr = "1" then
			set news_title to "A To-Do Added!"
			set news to "🔘 " & item 2 of argv
		else
			set news_title to nr & " To-Dos Added!"
		end if
	end if
	
	
	tell application "LaunchBar"
		display in notification center news with title news_title callback URL "things:///show?id=inbox"
	end tell
end run