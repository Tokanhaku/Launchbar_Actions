-- LaunchBar Action Script

activate application "QuickTime Player"
tell application "System Events"
	tell application "QuickTime Player"
		# set frontmost to true
		# click menu item "Neue Bildschirmaufnahme" of menu "Ablage" of menu bar 1
		# 等待「屏幕录制」窗口出现
		new screen recording
		# repeat until exists window "Bildschirmaufnahme"
		# end repeat
		# 按下空格键
		tell application "System Events" to keystroke " "
	end tell
end tell