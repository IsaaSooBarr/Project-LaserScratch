from Packets.Messages.Client.Home.AskPlayerJWTokenMessage import AskPlayerJWTokenMessage
from Packets.Messages.Client.Login.ClientCryptoErrorMessage import ClientCryptoErrorMessage
from Packets.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage
from Packets.Messages.Client.Login.LoginMessage import LoginMessage
from Packets.Messages.Client.Login.LoginUsingSessionMessage import LoginUsingSessionMessage
from Packets.Messages.Client.Login.CreateAccountMessage import CreateAccountMessage
from Packets.Messages.Client.Home.ClientCapabilitiesMessage import ClientCapabilitiesMessage
from Packets.Messages.Client.Home.KeepAliveMessage import KeepAliveMessage
from Packets.Messages.Client.Home.UdpCheckConnectionMessage import UdpCheckConnectionMessage
from Packets.Messages.Client.Home.AnalyticEventMessage import AnalyticEventMessage
from Packets.Messages.Client.Login.AuthenticationCheckMessage import AuthenticationCheckMessage
from Packets.Messages.Client.Login.SetDeviceTokenMessage import SetDeviceTokenMessage
from Packets.Messages.Client.Login.ResetAccountMessage import ResetAccountMessage
from Packets.Messages.Client.Battle.GoHomeMessage import GoHomeMessage
from Packets.Messages.Client.Home.ReportUserMessage import ReportUserMessage
from Packets.Messages.Client.Login.AccountSwitchedMessage import AccountSwitchedMessage
from Packets.Messages.Client.Alliance.ReportAllianceStreamMessage import ReportAllianceStreamMessage
from Packets.Messages.Client.Login.UnlockAccountMessage import UnlockAccountMessage
from Packets.Messages.Client.Billing.AppleBillingRequestMessage import AppleBillingRequestMessage
from Packets.Messages.Client.Billing.GoogleBillingRequestMessage import GoogleBillingRequestMessage
from Packets.Messages.Client.Billing.TencentBillingRequestMessage import TencentBillingRequestMessage
from Packets.Messages.Client.Billing.CafeBazaarBillingRequestMessage import CafeBazaarBillingRequestMessage
from Packets.Messages.Client.Billing.KunlunBillingRequestMessage import KunlunBillingRequestMessage
from Packets.Messages.Client.Billing.BillingCancelledByClientMessage import BillingCancelledByClientMessage
### TODO ###
from Packets.Messages.Client.Battle.MatchmakeRequestMessage import MatchmakeRequestMessage
from Packets.Messages.Client.Battle.CancelMatchMakingMessage import CancelMatchMakingMessage
from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Packets.Messages.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Packets.Messages.Client.Home.GetSeasonRewardsMessage import GetSeasonRewardsMessage
from Packets.Messages.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Packets.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage
from Packets.Messages.Client.Gameroom.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Packets.Messages.Client.Gameroom.TeamMemberStatusMessage import TeamMemberStatusMessage
from Packets.Messages.Client.Gameroom.TeamSetEventMessage import TeamSetEventMessage
from Packets.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.Home.PlayerStatusMessage import PlayerStatusMessage
from Packets.Messages.Client.Home.GetLeaderboardMessage import GetLeaderboardMessage


AvailablePackets = {
    10055: AskPlayerJWTokenMessage,
    10099: ClientCryptoErrorMessage,
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10102: LoginUsingSessionMessage,
    10103: CreateAccountMessage,
    10107: ClientCapabilitiesMessage,
    10108: KeepAliveMessage,
    10109: UdpCheckConnectionMessage,
    10110: AnalyticEventMessage,
    10112: AuthenticationCheckMessage,
    10113: SetDeviceTokenMessage,
    10116: ResetAccountMessage,
    10117: ReportUserMessage,
    10118: AccountSwitchedMessage,
    10119: ReportAllianceStreamMessage,
    10121: UnlockAccountMessage,
    10150: AppleBillingRequestMessage,
    10151: GoogleBillingRequestMessage,
    10152: TencentBillingRequestMessage,
    10153: CafeBazaarBillingRequestMessage,
    10159: KunlunBillingRequestMessage,
    10160: BillingCancelledByClientMessage,
    ### TODO ###
    14101: GoHomeMessage,
    14103: MatchmakeRequestMessage,
    14106: CancelMatchMakingMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
    14113: GetPlayerProfileMessage,
    14277: GetSeasonRewardsMessage,
    14302: AskForAllianceDataMessage,
    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14355: TeamSetMemberReadyMessage,
    14361: TeamMemberStatusMessage,
    14362: TeamSetEventMessage,
    14363: TeamSetLocationMessage,
    14366: PlayerStatusMessage,
    14403: GetLeaderboardMessage,
}
