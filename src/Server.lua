local LogSize = 20
local AnswerEverynMessages = 1
local NonAnsweredMessages = AnswerEverynMessages
local HttpService = game:GetService("HttpService")
local AppUrl = "YOUR URL HERE"
Log = {}


function HandleMessage(Player, Message)
	table.insert(Log, {nickname = Player.name, content = Message})
	print(HttpService:PostAsync(AppUrl, HttpService:JSONEncode(Log), Enum.HttpContentType.ApplicationJson, false))

end

game.Players.PlayerAdded:Connect(function(Player)
	Player.Chatted:Connect(function(Message)
		HandleMessage(Player, Message)
	end)
end)

