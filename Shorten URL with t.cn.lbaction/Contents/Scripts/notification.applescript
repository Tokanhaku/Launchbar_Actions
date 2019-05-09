on run argv
	set short_url to item 1 of argv
	set the clipboard to short_url
	tell application "LaunchBar"
		display in notification center short_url with title "Short URL Copied!"
	end tell
end run