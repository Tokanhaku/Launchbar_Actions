activate application "Preview"
tell application "System Events"
	tell process "Preview"
		# set frontmost to true
		click menu item "New from Clipboard" of menu "File" of menu bar 1
	end tell
end tell