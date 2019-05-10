on run argv
	set short_url to item 2 of argv
	set Title to item 1 of argv
	set the clipboard to short_url
	tell application "LaunchBar"
		display in notification center short_url with title Title
	end tell
end run