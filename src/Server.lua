local LogSize = 20
local AnswerEverynMessages = 5
local NonAnsweredMessages = AnswerEverynMessages
local HttpService = game:GetService("HttpService")
local AppUrl = "YOUR SERVER URL"
Log = {}


function HandleMessage(Player, Message)
	table.insert(Log, {Player = Player, Message = Message})
	if NonAnsweredMessages < AnswerEverynMessages then
		NonAnsweredMessages += 1
	else
		HttpService:PostAsync(AppUrl, HttpService:JSONEncode(Log), Enum.HttpContentType.ApplicationJson, false)
		NonAnsweredMessages = 0
	end
end

game.Players.PlayerAdded:Connect(function(Player)
	Player.Chatted:Connect(function(Message)
		HandleMessage(Player, Message)
	end)
end)

