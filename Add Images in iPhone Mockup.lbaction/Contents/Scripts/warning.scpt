-- Copyright (c) 2012 Objective Development
-- http://www.obdev.at/
-- Version 1

on run argv
	set filename to item 1 of argv
	set news_title to "This is not an iPad Pro Screenshot!"
	
	
	tell application "LaunchBar"
		display in notification center filename with title news_title callback URL "file://" & filename
	end tell
end run