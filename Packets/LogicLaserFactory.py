from Packets.Messages.Client.Login.ClientCryptoErrorMessage import ClientCryptoErrorMessage
from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage
from Packets.Messages.Client.Home.ClientCapabilitiesMessage import ClientCapabilitiesMessage
from Packets.Messages.Client.Home.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.Home.AnalyticsEventMessage import AnalyticsEventMessage
from Packets.Messages.Client.Battle.GoHomeMessage import GoHomeMessage
from Packets.Messages.Client.Battle.MatchmakeRequestMessage import MatchmakeRequestMessage
from Packets.Messages.Client.Battle.CancelMatchMakingMessage import CancelMatchMakingMessage
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Packets.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Packets.Messages.Client.Home.GetSeasonRewardsMessage import GetSeasonRewardsMessage
from Packets.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Packets.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Packets.Messages.Client.Home.GetLeaderboardMessage import GetLeaderboardMessage


AvailablePackets = {
    10099: ClientCryptoErrorMessage,
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10110: AnalyticsEventMessage,
    14101: GoHomeMessage,
    14103: MatchmakeRequestMessage,
    14106: CancelMatchMakingMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14277: GetSeasonRewardsMessage,
    14302: AskForAllianceDataMessage,
    14366: PlayerStatusMessage,
    14403: GetLeaderboardMessage,
}
