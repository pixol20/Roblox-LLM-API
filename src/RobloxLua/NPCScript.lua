local BotName = "Pepe"
local LogSize = 20
-- local AnswerEverynMessages = 1
-- local NonAnsweredMessages = AnswerEverynMessages
local HttpService = game:GetService("HttpService")
local ChatService = game:GetService("Chat")
local AppUrl = "YOUR URL HERE"
Log = {}


function HandleMessage(Player, Message)
	table.insert(Log, {nickname = Player.name, content = Message})
	local response = HttpService:PostAsync(AppUrl, HttpService:JSONEncode(Log), Enum.HttpContentType.ApplicationJson, false)
	game.ReplicatedStorage.ClientSendMsg:FireAllClients(BotName, response)
	table.insert(Log, {nickname = BotName, content = response})
	ChatService:Chat(script.Parent.Head, response)
end

game.Players.PlayerAdded:Connect(function(Player)
	Player.Chatted:Connect(function(Message)
		HandleMessage(Player, Message)
	end)
end)

