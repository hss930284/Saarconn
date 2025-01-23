#------------------------------------------------------------------------------
# Class metaEnum
#------------------------------------------------------------------------------
class metaENUM(type(int)):
	"""Base class for enums and bitmask. Initializes class members."""
	def __init__(cls, name, bases, namespace):
		'''Convert enumeration names into attributes'''
		names = namespace.get('_names_', {})
		if hasattr(names, 'keys'):
			for (k,v) in names.items():
				setattr(cls, k, cls(v))
				names[v]=k
		else:
			for (i,k) in enumerate(names):
				setattr(cls, k, cls(i))
		super(metaENUM, cls).__init__(name, bases, namespace)


#------------------------------------------------------------------------------
# Class ENUM
#------------------------------------------------------------------------------
class ENUM(int, metaclass=metaENUM):
	'''Enumeration base class. Set _names_ attribute to a list
	of enumeration names (counting from 0)
	or a dictionary of name:value pairs.'''
	def __str__(self):
		return self.__repr__(fmt="%(value)s")


	def __repr__(self, fmt="<%(name)s %(value)s>"):
		try:
			return self._names_[self]
		except:
			return fmt % dict(name=self.__class__.__name__, value=self)


#------------------------------------------------------------------------------
# Class CheckForDifferencesFileState
#------------------------------------------------------------------------------
class CheckForDifferencesFileState(ENUM):
	"""Defines CheckForDifferencesFileState Enums"""
	_names_ = """Identical Missing Different MinorDifferences """.split()


#------------------------------------------------------------------------------
# Class ArSchemas
#------------------------------------------------------------------------------
class ArSchemas(ENUM):
	"""Defines ArSchemas Enums"""
	_names_ = """Unknown Legacy Autosar302 Autosar304 Autosar306 Autosar307 Autosar310 Autosar312 Autosar314 Autosar314Dai Autosar315 Autosar321 Autosar401 Autosar402 Autosar403 Autosar411 Autosar412 Autosar413 Autosar421 Autosar422 Autosar430 Autosar431 Autosar440 Autosar00047 Autosar00048 Autosar00049 Autosar00050 Autosar00051 """.split()


#------------------------------------------------------------------------------
# Class AsyncReasonEnum
#------------------------------------------------------------------------------
class AsyncReasonEnum(ENUM):
	"""Defines AsyncReasonEnum Enums"""
	_names_ = """NONE SourceSystem EcuSystem UpdateError Imported """.split()


#------------------------------------------------------------------------------
# Class BaseTypeEnum
#------------------------------------------------------------------------------
class BaseTypeEnum(ENUM):
	"""Defines BaseTypeEnum Enums"""
	_names_ = """Unsupported Float32 Float64 SInt8 SInt16 SInt32 UInt8 UInt16 UInt32 Boolean String SInt64 UInt64 Void """.split()


#------------------------------------------------------------------------------
# Class BorderStyle
#------------------------------------------------------------------------------
class BorderStyle(ENUM):
	"""Defines BorderStyle Enums"""
	_names_ = """Dashed Dotted Solid """.split()


#------------------------------------------------------------------------------
# Class ConstantValuePattern
#------------------------------------------------------------------------------
class ConstantValuePattern(ENUM):
	"""Defines ConstantValuePattern Enums"""
	_names_ = """Empty Unsupported ApplicationScalar ApplicationArray InternalValue InternalStructure ReferenceToConstant ReferenceToDataPrototype Text ApplicationText NotAvailable Invalid """.split()


#------------------------------------------------------------------------------
# Class ConversionKind
#------------------------------------------------------------------------------
class ConversionKind(ENUM):
	"""Defines ConversionKind Enums"""
	_names_ = """Linear Texttable Table RationalScale RationalAndTexttable LinearAndTexttable LinearScale Rational Identical Unsupported BitfieldTexttable """.split()


#------------------------------------------------------------------------------
# Class Indexing
#------------------------------------------------------------------------------
class Indexing(ENUM):
	"""Defines Indexing Enums"""
	_names_ = """Increasing Decreasing """.split()


#------------------------------------------------------------------------------
# Class InterfaceClass
#------------------------------------------------------------------------------
class InterfaceClass(ENUM):
	"""Defines InterfaceClass Enums"""
	_names_ = """Provided Required """.split()


#------------------------------------------------------------------------------
# Class LabelAlignment
#------------------------------------------------------------------------------
class LabelAlignment(ENUM):
	"""Defines LabelAlignment Enums"""
	_names_ = """Bottom Center Left Right Top """.split()


#------------------------------------------------------------------------------
# Class ORTargetAccessErrorKind
#------------------------------------------------------------------------------
class ORTargetAccessErrorKind(ENUM):
	"""Defines ORTargetAccessErrorKind Enums"""
	_names_ = """TargetAvailable AUTOSARTargetDefinedButNotAvailable WrongDestinationType UndefinedReference AmbiguousReference NeverResolve """.split()


#------------------------------------------------------------------------------
# Class PropertyInheritanceEnum
#------------------------------------------------------------------------------
class PropertyInheritanceEnum(ENUM):
	"""Defines PropertyInheritanceEnum Enums"""
	_names_ = """NONE Inherit Redefine """.split()


#------------------------------------------------------------------------------
# Class TemporalErrorType
#------------------------------------------------------------------------------
class TemporalErrorType(ENUM):
	"""Defines TemporalErrorType Enums"""
	_names_ = """Permanent Sporadic """.split()


#------------------------------------------------------------------------------
# Class CustomValidationRuleResultEnum
#------------------------------------------------------------------------------
class CustomValidationRuleResultEnum(ENUM):
	"""Defines CustomValidationRuleResultEnum Enums"""
	_names_ = """OK SevereError Error Warning Information """.split()


#------------------------------------------------------------------------------
# Class ValidationOutcome
#------------------------------------------------------------------------------
class ValidationOutcome(ENUM):
	"""Defines ValidationOutcome Enums"""
	_names_ = """Error Warning Valid Aborted """.split()


#------------------------------------------------------------------------------
# Class FileType
#------------------------------------------------------------------------------
class FileType(ENUM):
	"""Defines FileType Enums"""
	_names_ = """Default SourceFile HeaderFile LibraryFile ObjectFile TargetResourceFile HostResourceFile GenericFile """.split()


#------------------------------------------------------------------------------
# Class InterventionPointKind
#------------------------------------------------------------------------------
class InterventionPointKind(ENUM):
	"""Defines InterventionPointKind Enums"""
	_names_ = """Read Status Write """.split()


#------------------------------------------------------------------------------
# Class InterventionPointKindOption
#------------------------------------------------------------------------------
class InterventionPointKindOption(ENUM):
	"""Defines InterventionPointKindOption Enums"""
	_names_ = """All ReadOnly WriteOnly ReadAndWriteOnly StatusOnly ReadAndStatusOnly WriteAndStatusOnly """.split()


#------------------------------------------------------------------------------
# Class InterventionServiceBehavior
#------------------------------------------------------------------------------
class InterventionServiceBehavior(ENUM):
	"""Defines InterventionServiceBehavior Enums"""
	_names_ = """ReadBeforeWrite WriteBeforeRead """.split()


#------------------------------------------------------------------------------
# Class InterventionServiceCustomCodeLocation
#------------------------------------------------------------------------------
class InterventionServiceCustomCodeLocation(ENUM):
	"""Defines InterventionServiceCustomCodeLocation Enums"""
	_names_ = """Top PreEnable PostEnable PreOutput PostOutput PreInput PostInput Bottom """.split()


#------------------------------------------------------------------------------
# Class InterventionServiceType
#------------------------------------------------------------------------------
class InterventionServiceType(ENUM):
	"""Defines InterventionServiceType Enums"""
	_names_ = """NONE DataAccessPoint RteServicePort """.split()


#------------------------------------------------------------------------------
# Class SystemDeskViewEnum
#------------------------------------------------------------------------------
class SystemDeskViewEnum(ENUM):
	"""Defines SystemDeskViewEnum Enums"""
	_names_ = """ProjectManager SystemManager EcuConfigurationManager VEcuManager """.split()


#------------------------------------------------------------------------------
# Class CanTpAddressingFormatTypeEnum
#------------------------------------------------------------------------------
class CanTpAddressingFormatTypeEnum(ENUM):
	"""Defines CanTpAddressingFormatTypeEnum Enums"""
	_names_ = """undefined Extended Mixed Mixed29Bit Normalfixed Standard """.split()


#------------------------------------------------------------------------------
# Class FrArTpAckTypeEnum
#------------------------------------------------------------------------------
class FrArTpAckTypeEnum(ENUM):
	"""Defines FrArTpAckTypeEnum Enums"""
	_names_ = """undefined AckWithRt AckWithoutRt NoAck """.split()


#------------------------------------------------------------------------------
# Class MaximumMessageLengthTypeEnum
#------------------------------------------------------------------------------
class MaximumMessageLengthTypeEnum(ENUM):
	"""Defines MaximumMessageLengthTypeEnum Enums"""
	_names_ = """undefined I4G Iso Iso6 """.split()


#------------------------------------------------------------------------------
# Class NetworkTargetAddressTypeEnum
#------------------------------------------------------------------------------
class NetworkTargetAddressTypeEnum(ENUM):
	"""Defines NetworkTargetAddressTypeEnum Enums"""
	_names_ = """undefined Functional Physical """.split()


#------------------------------------------------------------------------------
# Class TpAckTypeEnum
#------------------------------------------------------------------------------
class TpAckTypeEnum(ENUM):
	"""Defines TpAckTypeEnum Enums"""
	_names_ = """undefined AckWithRt NoAck """.split()


#------------------------------------------------------------------------------
# Class CSTransformerErrorReactionEnum
#------------------------------------------------------------------------------
class CSTransformerErrorReactionEnum(ENUM):
	"""Defines CSTransformerErrorReactionEnum Enums"""
	_names_ = """undefined ApplicationOnly Autonomous """.split()


#------------------------------------------------------------------------------
# Class DataIdModeEnum
#------------------------------------------------------------------------------
class DataIdModeEnum(ENUM):
	"""Defines DataIdModeEnum Enums"""
	_names_ = """undefined All16Bit Alternating8Bit Lower12Bit Lower8Bit """.split()


#------------------------------------------------------------------------------
# Class DataTransformationKindEnum
#------------------------------------------------------------------------------
class DataTransformationKindEnum(ENUM):
	"""Defines DataTransformationKindEnum Enums"""
	_names_ = """undefined AsymmetricFromByteArray AsymmetricToByteArray Symmetric """.split()


#------------------------------------------------------------------------------
# Class EndToEndProfileBehaviorEnum
#------------------------------------------------------------------------------
class EndToEndProfileBehaviorEnum(ENUM):
	"""Defines EndToEndProfileBehaviorEnum Enums"""
	_names_ = """undefined PreR42 R42 """.split()


#------------------------------------------------------------------------------
# Class SOMEIPMessageTypeEnum
#------------------------------------------------------------------------------
class SOMEIPMessageTypeEnum(ENUM):
	"""Defines SOMEIPMessageTypeEnum Enums"""
	_names_ = """undefined Notification Request RequestNoReturn Response """.split()


#------------------------------------------------------------------------------
# Class SOMEIPTransformerSessionHandlingEnum
#------------------------------------------------------------------------------
class SOMEIPTransformerSessionHandlingEnum(ENUM):
	"""Defines SOMEIPTransformerSessionHandlingEnum Enums"""
	_names_ = """undefined SessionHandlingActive SessionHandlingInactive """.split()


#------------------------------------------------------------------------------
# Class TransformerClassEnum
#------------------------------------------------------------------------------
class TransformerClassEnum(ENUM):
	"""Defines TransformerClassEnum Enums"""
	_names_ = """undefined Custom Safety Security Serializer """.split()


#------------------------------------------------------------------------------
# Class MappingScopeEnum
#------------------------------------------------------------------------------
class MappingScopeEnum(ENUM):
	"""Defines MappingScopeEnum Enums"""
	_names_ = """undefined MappingScopeCore MappingScopeEcu MappingScopePartition """.split()


#------------------------------------------------------------------------------
# Class DataConsistencyPolicyEnum
#------------------------------------------------------------------------------
class DataConsistencyPolicyEnum(ENUM):
	"""Defines DataConsistencyPolicyEnum Enums"""
	_names_ = """undefined ConsistencyMechanismRequired NoConsistencyMechanism """.split()


#------------------------------------------------------------------------------
# Class SendIndicationEnum
#------------------------------------------------------------------------------
class SendIndicationEnum(ENUM):
	"""Defines SendIndicationEnum Enums"""
	_names_ = """undefined AnySendOperation NONE """.split()


#------------------------------------------------------------------------------
# Class SwcToSwcOperationArgumentsDirectionEnum
#------------------------------------------------------------------------------
class SwcToSwcOperationArgumentsDirectionEnum(ENUM):
	"""Defines SwcToSwcOperationArgumentsDirectionEnum Enums"""
	_names_ = """undefined In Out """.split()


#------------------------------------------------------------------------------
# Class CryptoCertificateAlgorithmFamilyEnum
#------------------------------------------------------------------------------
class CryptoCertificateAlgorithmFamilyEnum(ENUM):
	"""Defines CryptoCertificateAlgorithmFamilyEnum Enums"""
	_names_ = """undefined Ecc Rsa """.split()


#------------------------------------------------------------------------------
# Class CryptoCertificateFormatEnum
#------------------------------------------------------------------------------
class CryptoCertificateFormatEnum(ENUM):
	"""Defines CryptoCertificateFormatEnum Enums"""
	_names_ = """undefined Cvc X509 """.split()


#------------------------------------------------------------------------------
# Class CryptoServiceKeyGenerationEnum
#------------------------------------------------------------------------------
class CryptoServiceKeyGenerationEnum(ENUM):
	"""Defines CryptoServiceKeyGenerationEnum Enums"""
	_names_ = """undefined KeyDerivation KeyStorage """.split()


#------------------------------------------------------------------------------
# Class IPsecDpdActionEnum
#------------------------------------------------------------------------------
class IPsecDpdActionEnum(ENUM):
	"""Defines IPsecDpdActionEnum Enums"""
	_names_ = """undefined Clear Restart Trap """.split()


#------------------------------------------------------------------------------
# Class IPsecHeaderTypeEnum
#------------------------------------------------------------------------------
class IPsecHeaderTypeEnum(ENUM):
	"""Defines IPsecHeaderTypeEnum Enums"""
	_names_ = """undefined Ah Esp NONE """.split()


#------------------------------------------------------------------------------
# Class IPsecIpProtocolEnum
#------------------------------------------------------------------------------
class IPsecIpProtocolEnum(ENUM):
	"""Defines IPsecIpProtocolEnum Enums"""
	_names_ = """undefined Any Icmp Tcp Udp """.split()


#------------------------------------------------------------------------------
# Class IPsecModeEnum
#------------------------------------------------------------------------------
class IPsecModeEnum(ENUM):
	"""Defines IPsecModeEnum Enums"""
	_names_ = """undefined Transport Tunnel """.split()


#------------------------------------------------------------------------------
# Class IPsecPolicyEnum
#------------------------------------------------------------------------------
class IPsecPolicyEnum(ENUM):
	"""Defines IPsecPolicyEnum Enums"""
	_names_ = """undefined Drop Ipsec Passthrough Reject """.split()


#------------------------------------------------------------------------------
# Class MacSecCapabilityEnum
#------------------------------------------------------------------------------
class MacSecCapabilityEnum(ENUM):
	"""Defines MacSecCapabilityEnum Enums"""
	_names_ = """undefined IntergrityAndConfidentiality IntergrityWithoutConfidentiality """.split()


#------------------------------------------------------------------------------
# Class MacSecConfidentialityOffsetEnum
#------------------------------------------------------------------------------
class MacSecConfidentialityOffsetEnum(ENUM):
	"""Defines MacSecConfidentialityOffsetEnum Enums"""
	_names_ = """undefined ConfidentialityOffset0 ConfidentialityOffset30 ConfidentialityOffset50 """.split()


#------------------------------------------------------------------------------
# Class MacSecFailPermissiveModeEnum
#------------------------------------------------------------------------------
class MacSecFailPermissiveModeEnum(ENUM):
	"""Defines MacSecFailPermissiveModeEnum Enums"""
	_names_ = """undefined Never Timeout """.split()


#------------------------------------------------------------------------------
# Class MacSecRoleEnum
#------------------------------------------------------------------------------
class MacSecRoleEnum(ENUM):
	"""Defines MacSecRoleEnum Enums"""
	_names_ = """undefined KeyServer Peer """.split()


#------------------------------------------------------------------------------
# Class TlsVersionEnum
#------------------------------------------------------------------------------
class TlsVersionEnum(ENUM):
	"""Defines TlsVersionEnum Enums"""
	_names_ = """undefined Tls12 Tls13 """.split()


#------------------------------------------------------------------------------
# Class OsTaskPreemptabilityEnum
#------------------------------------------------------------------------------
class OsTaskPreemptabilityEnum(ENUM):
	"""Defines OsTaskPreemptabilityEnum Enums"""
	_names_ = """undefined Full NONE """.split()


#------------------------------------------------------------------------------
# Class FlexrayNmScheduleVariantEnum
#------------------------------------------------------------------------------
class FlexrayNmScheduleVariantEnum(ENUM):
	"""Defines FlexrayNmScheduleVariantEnum Enums"""
	_names_ = """undefined ScheduleVariant1 ScheduleVariant2 ScheduleVariant3 ScheduleVariant4 ScheduleVariant5 ScheduleVariant6 ScheduleVariant7 """.split()


#------------------------------------------------------------------------------
# Class NmCoordinatorRoleEnum
#------------------------------------------------------------------------------
class NmCoordinatorRoleEnum(ENUM):
	"""Defines NmCoordinatorRoleEnum Enums"""
	_names_ = """undefined Active Passive """.split()


#------------------------------------------------------------------------------
# Class GlobalTimeCrcSupportEnum
#------------------------------------------------------------------------------
class GlobalTimeCrcSupportEnum(ENUM):
	"""Defines GlobalTimeCrcSupportEnum Enums"""
	_names_ = """undefined CrcNotSupported CrcSupported """.split()


#------------------------------------------------------------------------------
# Class GlobalTimeCrcValidationEnum
#------------------------------------------------------------------------------
class GlobalTimeCrcValidationEnum(ENUM):
	"""Defines GlobalTimeCrcValidationEnum Enums"""
	_names_ = """undefined CrcIgnored CrcNotValidated CrcOptional CrcValidated """.split()


#------------------------------------------------------------------------------
# Class GlobalTimeIcvSupportEnum
#------------------------------------------------------------------------------
class GlobalTimeIcvSupportEnum(ENUM):
	"""Defines GlobalTimeIcvSupportEnum Enums"""
	_names_ = """undefined IcvNotSupported IcvSupported """.split()


#------------------------------------------------------------------------------
# Class GlobalTimeIcvVerificationEnum
#------------------------------------------------------------------------------
class GlobalTimeIcvVerificationEnum(ENUM):
	"""Defines GlobalTimeIcvVerificationEnum Enums"""
	_names_ = """undefined IcvIgnored IcvNotVerified IcvOptional IcvVerified """.split()


#------------------------------------------------------------------------------
# Class EthGlobalTimeMessageFormatEnum
#------------------------------------------------------------------------------
class EthGlobalTimeMessageFormatEnum(ENUM):
	"""Defines EthGlobalTimeMessageFormatEnum Enums"""
	_names_ = """undefined Ieee8021As Ieee8021AsAutosar """.split()


#------------------------------------------------------------------------------
# Class CommunicationDirectionTypeEnum
#------------------------------------------------------------------------------
class CommunicationDirectionTypeEnum(ENUM):
	"""Defines CommunicationDirectionTypeEnum Enums"""
	_names_ = """undefined In Out """.split()


#------------------------------------------------------------------------------
# Class ContainedIPduCollectionSemanticsEnum
#------------------------------------------------------------------------------
class ContainedIPduCollectionSemanticsEnum(ENUM):
	"""Defines ContainedIPduCollectionSemanticsEnum Enums"""
	_names_ = """undefined LastIsBest Queued """.split()


#------------------------------------------------------------------------------
# Class ContainerIPduHeaderTypeEnum
#------------------------------------------------------------------------------
class ContainerIPduHeaderTypeEnum(ENUM):
	"""Defines ContainerIPduHeaderTypeEnum Enums"""
	_names_ = """undefined LongHeader NoHeader ShortHeader """.split()


#------------------------------------------------------------------------------
# Class ContainerIPduTriggerEnum
#------------------------------------------------------------------------------
class ContainerIPduTriggerEnum(ENUM):
	"""Defines ContainerIPduTriggerEnum Enums"""
	_names_ = """undefined DefaultTrigger FirstContainedTrigger """.split()


#------------------------------------------------------------------------------
# Class CycleRepetitionTypeEnum
#------------------------------------------------------------------------------
class CycleRepetitionTypeEnum(ENUM):
	"""Defines CycleRepetitionTypeEnum Enums"""
	_names_ = """undefined CycleRepetition1 CycleRepetition10 CycleRepetition16 CycleRepetition2 CycleRepetition20 CycleRepetition32 CycleRepetition4 CycleRepetition40 CycleRepetition5 CycleRepetition50 CycleRepetition64 CycleRepetition8 """.split()


#------------------------------------------------------------------------------
# Class DiagPduTypeEnum
#------------------------------------------------------------------------------
class DiagPduTypeEnum(ENUM):
	"""Defines DiagPduTypeEnum Enums"""
	_names_ = """undefined DiagRequest DiagResponse """.split()


#------------------------------------------------------------------------------
# Class IPduSignalProcessingEnum
#------------------------------------------------------------------------------
class IPduSignalProcessingEnum(ENUM):
	"""Defines IPduSignalProcessingEnum Enums"""
	_names_ = """undefined Deferred Immediate """.split()


#------------------------------------------------------------------------------
# Class PncGatewayTypeEnum
#------------------------------------------------------------------------------
class PncGatewayTypeEnum(ENUM):
	"""Defines PncGatewayTypeEnum Enums"""
	_names_ = """undefined Active NONE Passive """.split()


#------------------------------------------------------------------------------
# Class RxAcceptContainedIPduEnum
#------------------------------------------------------------------------------
class RxAcceptContainedIPduEnum(ENUM):
	"""Defines RxAcceptContainedIPduEnum Enums"""
	_names_ = """undefined AcceptAll AcceptConfigured """.split()


#------------------------------------------------------------------------------
# Class SecuredPduHeaderEnum
#------------------------------------------------------------------------------
class SecuredPduHeaderEnum(ENUM):
	"""Defines SecuredPduHeaderEnum Enums"""
	_names_ = """undefined NoHeader SecuredPduHeader08Bit SecuredPduHeader16Bit SecuredPduHeader32Bit """.split()


#------------------------------------------------------------------------------
# Class TransferPropertyEnum
#------------------------------------------------------------------------------
class TransferPropertyEnum(ENUM):
	"""Defines TransferPropertyEnum Enums"""
	_names_ = """undefined Pending Triggered TriggeredOnChange TriggeredOnChangeWithoutRepetition TriggeredWithoutRepetition """.split()


#------------------------------------------------------------------------------
# Class TriggerModeEnum
#------------------------------------------------------------------------------
class TriggerModeEnum(ENUM):
	"""Defines TriggerModeEnum Enums"""
	_names_ = """undefined DynamicPartTrigger NONE StaticOrDynamicPartTrigger StaticPartTrigger """.split()


#------------------------------------------------------------------------------
# Class V2xSupportEnum
#------------------------------------------------------------------------------
class V2xSupportEnum(ENUM):
	"""Defines V2xSupportEnum Enums"""
	_names_ = """undefined V2XActiveSupported V2XNotSupported """.split()


#------------------------------------------------------------------------------
# Class ISignalTypeEnum
#------------------------------------------------------------------------------
class ISignalTypeEnum(ENUM):
	"""Defines ISignalTypeEnum Enums"""
	_names_ = """undefined Array Primitive """.split()


#------------------------------------------------------------------------------
# Class TtcanTriggerTypeEnum
#------------------------------------------------------------------------------
class TtcanTriggerTypeEnum(ENUM):
	"""Defines TtcanTriggerTypeEnum Enums"""
	_names_ = """undefined RxTrigger TxRefTrigger TxRefTriggerGap TxTriggerMerged TxTriggerSingle WatchTrigger WatchTriggerGap """.split()


#------------------------------------------------------------------------------
# Class LinChecksumTypeEnum
#------------------------------------------------------------------------------
class LinChecksumTypeEnum(ENUM):
	"""Defines LinChecksumTypeEnum Enums"""
	_names_ = """undefined Classic Enhanced """.split()


#------------------------------------------------------------------------------
# Class ResumePositionEnum
#------------------------------------------------------------------------------
class ResumePositionEnum(ENUM):
	"""Defines ResumePositionEnum Enums"""
	_names_ = """undefined ContinueAtItPosition StartFromBeginning """.split()


#------------------------------------------------------------------------------
# Class RunModeEnum
#------------------------------------------------------------------------------
class RunModeEnum(ENUM):
	"""Defines RunModeEnum Enums"""
	_names_ = """undefined RunContinuous RunOnce """.split()


#------------------------------------------------------------------------------
# Class FlexrayChannelNameEnum
#------------------------------------------------------------------------------
class FlexrayChannelNameEnum(ENUM):
	"""Defines FlexrayChannelNameEnum Enums"""
	_names_ = """undefined ChannelA ChannelB """.split()


#------------------------------------------------------------------------------
# Class CouplingElementEnum
#------------------------------------------------------------------------------
class CouplingElementEnum(ENUM):
	"""Defines CouplingElementEnum Enums"""
	_names_ = """undefined Hub Router Switch """.split()


#------------------------------------------------------------------------------
# Class DoIpEntityRoleEnum
#------------------------------------------------------------------------------
class DoIpEntityRoleEnum(ENUM):
	"""Defines DoIpEntityRoleEnum Enums"""
	_names_ = """undefined EdgeNode Gateway Node """.split()


#------------------------------------------------------------------------------
# Class EthernetConnectionNegotiationEnum
#------------------------------------------------------------------------------
class EthernetConnectionNegotiationEnum(ENUM):
	"""Defines EthernetConnectionNegotiationEnum Enums"""
	_names_ = """undefined Auto Master Slave """.split()


#------------------------------------------------------------------------------
# Class EthernetCouplingPortSchedulerEnum
#------------------------------------------------------------------------------
class EthernetCouplingPortSchedulerEnum(ENUM):
	"""Defines EthernetCouplingPortSchedulerEnum Enums"""
	_names_ = """undefined DeficitRoundRobin StrictPriority WeightedRoundRobin """.split()


#------------------------------------------------------------------------------
# Class EthernetPhysicalLayerTypeEnum
#------------------------------------------------------------------------------
class EthernetPhysicalLayerTypeEnum(ENUM):
	"""Defines EthernetPhysicalLayerTypeEnum Enums"""
	_names_ = """undefined _1000BaseT _1000BaseT1 _100BaseT1 _100BaseTx _10BaseT1S Ieee80211P """.split()


#------------------------------------------------------------------------------
# Class EthernetSwitchVlanEgressTaggingEnum
#------------------------------------------------------------------------------
class EthernetSwitchVlanEgressTaggingEnum(ENUM):
	"""Defines EthernetSwitchVlanEgressTaggingEnum Enums"""
	_names_ = """undefined NotSent SentTagged SentUntagged """.split()


#------------------------------------------------------------------------------
# Class EventGroupControlTypeEnum
#------------------------------------------------------------------------------
class EventGroupControlTypeEnum(ENUM):
	"""Defines EventGroupControlTypeEnum Enums"""
	_names_ = """undefined ActivationAndTriggerUnicast ActivationMulticast ActivationUnicast TriggerUnicast """.split()


#------------------------------------------------------------------------------
# Class IpAddressKeepEnum
#------------------------------------------------------------------------------
class IpAddressKeepEnum(ENUM):
	"""Defines IpAddressKeepEnum Enums"""
	_names_ = """undefined Forget StorePersistently """.split()


#------------------------------------------------------------------------------
# Class Ipv4AddressSourceEnum
#------------------------------------------------------------------------------
class Ipv4AddressSourceEnum(ENUM):
	"""Defines Ipv4AddressSourceEnum Enums"""
	_names_ = """undefined AutoIp AutoIpDoip Dhcpv4 Fixed """.split()


#------------------------------------------------------------------------------
# Class Ipv6AddressSourceEnum
#------------------------------------------------------------------------------
class Ipv6AddressSourceEnum(ENUM):
	"""Defines Ipv6AddressSourceEnum Enums"""
	_names_ = """undefined Dhcpv6 Fixed LinkLocal LinkLocalDoip RouterAdvertisement """.split()


#------------------------------------------------------------------------------
# Class PduCollectionTriggerEnum
#------------------------------------------------------------------------------
class PduCollectionTriggerEnum(ENUM):
	"""Defines PduCollectionTriggerEnum Enums"""
	_names_ = """undefined Always Never """.split()


#------------------------------------------------------------------------------
# Class RequestMethodEnum
#------------------------------------------------------------------------------
class RequestMethodEnum(ENUM):
	"""Defines RequestMethodEnum Enums"""
	_names_ = """undefined Connect Delete Get Head Options Post Put Trace """.split()


#------------------------------------------------------------------------------
# Class RuntimeAddressConfigurationEnum
#------------------------------------------------------------------------------
class RuntimeAddressConfigurationEnum(ENUM):
	"""Defines RuntimeAddressConfigurationEnum Enums"""
	_names_ = """undefined NONE Sd """.split()


#------------------------------------------------------------------------------
# Class TimeSyncTechnologyEnum
#------------------------------------------------------------------------------
class TimeSyncTechnologyEnum(ENUM):
	"""Defines TimeSyncTechnologyEnum Enums"""
	_names_ = """undefined AvbIeee8021As NtpRfc958 PtpIeee15882002 PtpIeee15882008 """.split()


#------------------------------------------------------------------------------
# Class ServiceVersionAcceptanceKindEnum
#------------------------------------------------------------------------------
class ServiceVersionAcceptanceKindEnum(ENUM):
	"""Defines ServiceVersionAcceptanceKindEnum Enums"""
	_names_ = """undefined ExactOrAnyMinorVersion MinimumMinorVersion """.split()


#------------------------------------------------------------------------------
# Class TcpRoleEnum
#------------------------------------------------------------------------------
class TcpRoleEnum(ENUM):
	"""Defines TcpRoleEnum Enums"""
	_names_ = """undefined Connect Listen """.split()


#------------------------------------------------------------------------------
# Class CouplingPortRatePolicyActionEnum
#------------------------------------------------------------------------------
class CouplingPortRatePolicyActionEnum(ENUM):
	"""Defines CouplingPortRatePolicyActionEnum Enums"""
	_names_ = """undefined BlockSource DropFrame """.split()


#------------------------------------------------------------------------------
# Class CouplingPortRoleEnum
#------------------------------------------------------------------------------
class CouplingPortRoleEnum(ENUM):
	"""Defines CouplingPortRoleEnum Enums"""
	_names_ = """undefined HostPort StandardPort UpLinkPort """.split()


#------------------------------------------------------------------------------
# Class EthernetMacLayerTypeEnum
#------------------------------------------------------------------------------
class EthernetMacLayerTypeEnum(ENUM):
	"""Defines EthernetMacLayerTypeEnum Enums"""
	_names_ = """undefined XMii XgMii XxgMii """.split()


#------------------------------------------------------------------------------
# Class EthernetSwitchVlanIngressTagEnum
#------------------------------------------------------------------------------
class EthernetSwitchVlanIngressTagEnum(ENUM):
	"""Defines EthernetSwitchVlanIngressTagEnum Enums"""
	_names_ = """undefined DropUntagged ForwardAsIs """.split()


#------------------------------------------------------------------------------
# Class PduCollectionSemanticsEnum
#------------------------------------------------------------------------------
class PduCollectionSemanticsEnum(ENUM):
	"""Defines PduCollectionSemanticsEnum Enums"""
	_names_ = """undefined LastIsBest Queued """.split()


#------------------------------------------------------------------------------
# Class UdpChecksumCalculationEnum
#------------------------------------------------------------------------------
class UdpChecksumCalculationEnum(ENUM):
	"""Defines UdpChecksumCalculationEnum Enums"""
	_names_ = """undefined UdpChecksumDisabled UdpChecksumEnabled """.split()


#------------------------------------------------------------------------------
# Class CanAddressingModeTypeEnum
#------------------------------------------------------------------------------
class CanAddressingModeTypeEnum(ENUM):
	"""Defines CanAddressingModeTypeEnum Enums"""
	_names_ = """undefined Extended Standard """.split()


#------------------------------------------------------------------------------
# Class CanFrameRxBehaviorEnum
#------------------------------------------------------------------------------
class CanFrameRxBehaviorEnum(ENUM):
	"""Defines CanFrameRxBehaviorEnum Enums"""
	_names_ = """undefined Any Can20 CanFd """.split()


#------------------------------------------------------------------------------
# Class CanFrameTxBehaviorEnum
#------------------------------------------------------------------------------
class CanFrameTxBehaviorEnum(ENUM):
	"""Defines CanFrameTxBehaviorEnum Enums"""
	_names_ = """undefined Can20 CanFd """.split()


#------------------------------------------------------------------------------
# Class DltDefaultTraceStateEnum
#------------------------------------------------------------------------------
class DltDefaultTraceStateEnum(ENUM):
	"""Defines DltDefaultTraceStateEnum Enums"""
	_names_ = """undefined DefaultTraceStateDisabled DefaultTraceStateEnabled """.split()


#------------------------------------------------------------------------------
# Class DataTypePolicyEnum
#------------------------------------------------------------------------------
class DataTypePolicyEnum(ENUM):
	"""Defines DataTypePolicyEnum Enums"""
	_names_ = """undefined Legacy NetworkRepresentationFromComSpec Override TransformingISignal """.split()


#------------------------------------------------------------------------------
# Class DataTransformationErrorHandlingEnum
#------------------------------------------------------------------------------
class DataTransformationErrorHandlingEnum(ENUM):
	"""Defines DataTransformationErrorHandlingEnum Enums"""
	_names_ = """undefined NoTransformerErrorHandling TransformerErrorHandling """.split()


#------------------------------------------------------------------------------
# Class HandleTerminationAndRestartEnum
#------------------------------------------------------------------------------
class HandleTerminationAndRestartEnum(ENUM):
	"""Defines HandleTerminationAndRestartEnum Enums"""
	_names_ = """undefined CanBeTerminated CanBeTerminatedAndRestarted NoSupport """.split()


#------------------------------------------------------------------------------
# Class VariableAccessScopeEnum
#------------------------------------------------------------------------------
class VariableAccessScopeEnum(ENUM):
	"""Defines VariableAccessScopeEnum Enums"""
	_names_ = """undefined CommunicationInterEcu CommunicationIntraPartition InterPartitionIntraEcu """.split()


#------------------------------------------------------------------------------
# Class DataTransformationStatusForwardingEnum
#------------------------------------------------------------------------------
class DataTransformationStatusForwardingEnum(ENUM):
	"""Defines DataTransformationStatusForwardingEnum Enums"""
	_names_ = """undefined NoTransformerStatusForwarding TransformerStatusForwarding """.split()


#------------------------------------------------------------------------------
# Class SupportBufferLockingEnum
#------------------------------------------------------------------------------
class SupportBufferLockingEnum(ENUM):
	"""Defines SupportBufferLockingEnum Enums"""
	_names_ = """undefined DoesNotSupportBufferLocking SupportsBufferLocking """.split()


#------------------------------------------------------------------------------
# Class RteApiReturnValueProvisionEnum
#------------------------------------------------------------------------------
class RteApiReturnValueProvisionEnum(ENUM):
	"""Defines RteApiReturnValueProvisionEnum Enums"""
	_names_ = """undefined NoReturnValueProvided ReturnValueProvided """.split()


#------------------------------------------------------------------------------
# Class RptServicePointEnum
#------------------------------------------------------------------------------
class RptServicePointEnum(ENUM):
	"""Defines RptServicePointEnum Enums"""
	_names_ = """undefined Enabled NONE """.split()


#------------------------------------------------------------------------------
# Class MappingDirectionEnum
#------------------------------------------------------------------------------
class MappingDirectionEnum(ENUM):
	"""Defines MappingDirectionEnum Enums"""
	_names_ = """undefined Bidirectional FirstToSecond SecondToFirst """.split()


#------------------------------------------------------------------------------
# Class ServerArgumentImplPolicyEnum
#------------------------------------------------------------------------------
class ServerArgumentImplPolicyEnum(ENUM):
	"""Defines ServerArgumentImplPolicyEnum Enums"""
	_names_ = """undefined UseArgumentType UseVoid """.split()


#------------------------------------------------------------------------------
# Class RamBlockStatusControlEnum
#------------------------------------------------------------------------------
class RamBlockStatusControlEnum(ENUM):
	"""Defines RamBlockStatusControlEnum Enums"""
	_names_ = """undefined Api NvRamManager """.split()


#------------------------------------------------------------------------------
# Class ArraySizeHandlingEnum
#------------------------------------------------------------------------------
class ArraySizeHandlingEnum(ENUM):
	"""Defines ArraySizeHandlingEnum Enums"""
	_names_ = """undefined AllIndicesDifferentArraySize AllIndicesSameArraySize InheritedFromArrayElementTypeSize """.split()


#------------------------------------------------------------------------------
# Class HandleInvalidEnum
#------------------------------------------------------------------------------
class HandleInvalidEnum(ENUM):
	"""Defines HandleInvalidEnum Enums"""
	_names_ = """undefined DontInvalidate ExternalReplacement Keep Replace """.split()


#------------------------------------------------------------------------------
# Class HandleOutOfRangeEnum
#------------------------------------------------------------------------------
class HandleOutOfRangeEnum(ENUM):
	"""Defines HandleOutOfRangeEnum Enums"""
	_names_ = """undefined Default ExternalReplacement Ignore Invalid NONE Saturate """.split()


#------------------------------------------------------------------------------
# Class HandleOutOfRangeStatusEnum
#------------------------------------------------------------------------------
class HandleOutOfRangeStatusEnum(ENUM):
	"""Defines HandleOutOfRangeStatusEnum Enums"""
	_names_ = """undefined Indicate Silent """.split()


#------------------------------------------------------------------------------
# Class HandleTimeoutEnum
#------------------------------------------------------------------------------
class HandleTimeoutEnum(ENUM):
	"""Defines HandleTimeoutEnum Enums"""
	_names_ = """undefined NONE Replace ReplaceByTimeoutSubstitutionValue """.split()


#------------------------------------------------------------------------------
# Class TransmissionModeDefinitionEnum
#------------------------------------------------------------------------------
class TransmissionModeDefinitionEnum(ENUM):
	"""Defines TransmissionModeDefinitionEnum Enums"""
	_names_ = """undefined Cyclic CyclicAndOnChange Triggered """.split()


#------------------------------------------------------------------------------
# Class DataLimitKindEnum
#------------------------------------------------------------------------------
class DataLimitKindEnum(ENUM):
	"""Defines DataLimitKindEnum Enums"""
	_names_ = """undefined Max Min NONE """.split()


#------------------------------------------------------------------------------
# Class FilterDebouncingEnum
#------------------------------------------------------------------------------
class FilterDebouncingEnum(ENUM):
	"""Defines FilterDebouncingEnum Enums"""
	_names_ = """undefined DebounceData RawData WaitTimeDate """.split()


#------------------------------------------------------------------------------
# Class ProcessingKindEnum
#------------------------------------------------------------------------------
class ProcessingKindEnum(ENUM):
	"""Defines ProcessingKindEnum Enums"""
	_names_ = """undefined Filtered NONE Raw """.split()


#------------------------------------------------------------------------------
# Class PulseTestEnum
#------------------------------------------------------------------------------
class PulseTestEnum(ENUM):
	"""Defines PulseTestEnum Enums"""
	_names_ = """undefined Disable Enable """.split()


#------------------------------------------------------------------------------
# Class SignalFanEnum
#------------------------------------------------------------------------------
class SignalFanEnum(ENUM):
	"""Defines SignalFanEnum Enums"""
	_names_ = """undefined Nfold Single """.split()


#------------------------------------------------------------------------------
# Class DataExchangePointKindEnum
#------------------------------------------------------------------------------
class DataExchangePointKindEnum(ENUM):
	"""Defines DataExchangePointKindEnum Enums"""
	_names_ = """undefined Agreed Consumer Producer """.split()


#------------------------------------------------------------------------------
# Class SeverityEnum
#------------------------------------------------------------------------------
class SeverityEnum(ENUM):
	"""Defines SeverityEnum Enums"""
	_names_ = """undefined Error Info Warning """.split()


#------------------------------------------------------------------------------
# Class DefaultValueApplicationStrategyEnum
#------------------------------------------------------------------------------
class DefaultValueApplicationStrategyEnum(ENUM):
	"""Defines DefaultValueApplicationStrategyEnum Enums"""
	_names_ = """undefined DefaultIfRevisionUpdate DefaultIfUndefined NoDefault """.split()


#------------------------------------------------------------------------------
# Class SecurityEventContextDataSourceEnum
#------------------------------------------------------------------------------
class SecurityEventContextDataSourceEnum(ENUM):
	"""Defines SecurityEventContextDataSourceEnum Enums"""
	_names_ = """undefined UseFirstContextData UseLastContextData """.split()


#------------------------------------------------------------------------------
# Class SecurityEventReportingModeEnum
#------------------------------------------------------------------------------
class SecurityEventReportingModeEnum(ENUM):
	"""Defines SecurityEventReportingModeEnum Enums"""
	_names_ = """undefined Brief BriefBypassingFilters Detailed DetailedBypassingFilters Off """.split()


#------------------------------------------------------------------------------
# Class BindingTimeEnum
#------------------------------------------------------------------------------
class BindingTimeEnum(ENUM):
	"""Defines BindingTimeEnum Enums"""
	_names_ = """undefined CodeGenerationTime LinkTime PreCompileTime SystemDesignTime """.split()


#------------------------------------------------------------------------------
# Class AclScopeEnum
#------------------------------------------------------------------------------
class AclScopeEnum(ENUM):
	"""Defines AclScopeEnum Enums"""
	_names_ = """undefined Dependant Descendant Explicit """.split()


#------------------------------------------------------------------------------
# Class ArgumentDirectionEnum
#------------------------------------------------------------------------------
class ArgumentDirectionEnum(ENUM):
	"""Defines ArgumentDirectionEnum Enums"""
	_names_ = """undefined In Inout Out """.split()


#------------------------------------------------------------------------------
# Class AutoCollectEnum
#------------------------------------------------------------------------------
class AutoCollectEnum(ENUM):
	"""Defines AutoCollectEnum Enums"""
	_names_ = """undefined RefAll RefNonStandard RefNone """.split()


#------------------------------------------------------------------------------
# Class ByteOrderEnum
#------------------------------------------------------------------------------
class ByteOrderEnum(ENUM):
	"""Defines ByteOrderEnum Enums"""
	_names_ = """undefined MostSignificantByteFirst MostSignificantByteLast Opaque """.split()


#------------------------------------------------------------------------------
# Class MonotonyEnum
#------------------------------------------------------------------------------
class MonotonyEnum(ENUM):
	"""Defines MonotonyEnum Enums"""
	_names_ = """undefined Decreasing Increasing Monotonous NoMonotony StrictMonotonous StrictlyDecreasing StrictlyIncreasing """.split()


#------------------------------------------------------------------------------
# Class ReferrableSubtypesEnum
#------------------------------------------------------------------------------
class ReferrableSubtypesEnum(ENUM):
	"""Defines ReferrableSubtypesEnum Enums"""
	_names_ = """undefined AbstractAccessPoint AbstractCanCluster AbstractCanCommunicationConnector AbstractCanCommunicationController AbstractCanPhysicalChannel AbstractClassTailoring AbstractDoIpLogicAddressProps AbstractEthernetFrame AbstractEvent AbstractExecutionContext AbstractIamRemoteSubject AbstractImplementationDataType AbstractImplementationDataTypeElement AbstractProvidedPortPrototype AbstractRawDataStreamInterface AbstractRequiredPortPrototype AbstractSecurityEventFilter AbstractSecurityIdsmInstanceFilter AbstractServiceInstance AbstractSignalBasedToISignalTriggeringMapping AbstractSynchronizedTimeBaseInterface AclObjectSet AclOperation AclPermission AclRole AdaptiveApplicationSwComponentType AdaptiveFirewallModuleInstantiation AdaptiveFirewallToPortPrototypeMapping AdaptiveModuleInstantiation AdaptivePlatformServiceInstance AdaptiveSwcInternalBehavior AgeConstraint AggregationTailoring AliasNameSet AliveSupervision Allocator AnalyzedExecutionTime ApApplicationEndpoint ApApplicationError ApApplicationErrorDomain ApApplicationErrorSet ApSomeipTransformationProps AppOsTaskProxyToEcuTaskProxyMapping ApplicationArrayDataType ApplicationArrayElement ApplicationAssocMapDataType ApplicationAssocMapElement ApplicationCompositeDataType ApplicationCompositeElementDataPrototype ApplicationDataType ApplicationDeferredDataType ApplicationEndpoint ApplicationError ApplicationInterface ApplicationPartition ApplicationPartitionToEcuPartitionMapping ApplicationPrimitiveDataType ApplicationRecordDataType ApplicationRecordElement ApplicationSwComponentType ArElement ArPackage ArbitraryEventTriggering ArgumentDataPrototype ArtifactChecksum ArtifactChecksumToCryptoProviderMapping ArtifactLocator AssemblySwConnector AsynchronousServerCallPoint AsynchronousServerCallResultPoint AsynchronousServerCallReturnsEvent AtomicSwComponentType AtpBlueprint AtpBlueprintable AtpClassifier AtpDefinition AtpFeature AtpPrototype AtpStructureElement AtpType AttributeTailoring AutosarDataPrototype AutosarDataType AutosarOperationArgumentInstance AutosarVariableInstance BackgroundEvent BaseType BinaryManifestAddressableObject BinaryManifestItem BinaryManifestItemDefinition BinaryManifestMetaDataField BinaryManifestProvideResource BinaryManifestRequireResource BinaryManifestResource BinaryManifestResourceDefinition BlockState BlueprintMappingSet BswAsynchronousServerCallPoint BswAsynchronousServerCallResultPoint BswAsynchronousServerCallReturnsEvent BswBackgroundEvent BswCalledEntity BswCompositionTiming BswDataReceivedEvent BswDirectCallPoint BswDistinguishedPartition BswEntryRelationshipSet BswEvent BswExternalTriggerOccurredEvent BswImplementation BswInternalBehavior BswInternalTriggerOccurredEvent BswInternalTriggeringPoint BswInterruptEntity BswMgrNeeds BswModeManagerErrorEvent BswModeSwitchEvent BswModeSwitchedAckEvent BswModuleCallPoint BswModuleClientServerEntry BswModuleDependency BswModuleDescription BswModuleEntity BswModuleEntry BswModuleTiming BswOperationInvokedEvent BswOsTaskExecutionEvent BswSchedulableEntity BswScheduleEvent BswSchedulerNamePrefix BswServiceDependencyIdent BswSynchronousServerCallPoint BswTimingEvent BswVariableAccess BuildAction BuildActionEntity BuildActionEnvironment BuildActionManifest BulkNvDataDescriptor BurstPatternEventTriggering BusMirrorChannelMapping BusMirrorChannelMappingCan BusMirrorChannelMappingFlexray BusMirrorChannelMappingIp BusMirrorChannelMappingUserDefined CalibrationParameterValueSet CanCluster CanCommunicationConnector CanCommunicationController CanFrame CanFrameTriggering CanNmCluster CanNmNode CanPhysicalChannel CanTpAddress CanTpChannel CanTpConfig CanTpNode CanXlProps Caption Chapter CheckpointTransition ClassContentConditional ClientIdDefinition ClientIdDefinitionSet ClientServerInterface ClientServerInterfaceMapping ClientServerInterfaceToBswModuleEntryBlueprintMapping ClientServerOperation Code CollectableElement Collection ComCertificateToCryptoCertificateMapping ComEventGrant ComEventGrantDesign ComFieldGrant ComFieldGrantDesign ComFindServiceGrant ComFindServiceGrantDesign ComGrant ComGrantDesign ComKeyToCryptoKeySlotMapping ComManagementMapping ComMethodGrant ComMethodGrantDesign ComMgrUserNeeds ComOfferServiceGrant ComOfferServiceGrantDesign ComSecOcToCryptoKeySlotMapping ComTriggerGrantDesign CommConnectorPort CommunicationCluster CommunicationConnector CommunicationController Compiler ComplexDeviceDriverSwComponentType CompositionPPortToExecutablePPortMapping CompositionPortToExecutablePortMapping CompositionRPortToExecutableRPortMapping CompositionSwComponentType CompuMethod ConcreteClassTailoring ConcretePatternEventTriggering ConsistencyNeeds ConsistencyNeedsBlueprintSet ConstantSpecification ConstantSpecificationMappingSet ConstraintTailoring ConsumedEventGroup ConsumedProvidedServiceInstanceGroup ConsumedServiceInstance ContainerIPdu CouplingElement CouplingPort CouplingPortFifo CouplingPortScheduler CouplingPortShaper CouplingPortStructuralElement CouplingPortTrafficClassAssignment CpSoftwareCluster CpSoftwareClusterBinaryManifestDescriptor CpSoftwareClusterCommunicationResource CpSoftwareClusterMappingSet CpSoftwareClusterResource CpSoftwareClusterResourcePool CpSoftwareClusterResourceToApplicationPartitionMapping CpSoftwareClusterServiceResource CpSoftwareClusterToEcuInstanceMapping CpSoftwareClusterToResourceMapping CpSwClusterResourceToDiagDataElemMapping CpSwClusterResourceToDiagFunctionIdMapping CpSwClusterToDiagEventMapping CpSwClusterToDiagRoutineSubfunctionMapping CppImplementationDataType CppImplementationDataTypeContextTarget CppImplementationDataTypeElement CryptoCertificate CryptoCertificateInterface CryptoCertificateKeySlotNeeds CryptoCertificateToPortPrototypeMapping CryptoEllipticCurveProps CryptoInterface CryptoKeyManagementNeeds CryptoKeySlot CryptoKeySlotInterface CryptoKeySlotToPortPrototypeMapping CryptoModuleInstantiation CryptoNeeds CryptoProvider CryptoProviderInterface CryptoProviderToPortPrototypeMapping CryptoServiceCertificate CryptoServiceJobNeeds CryptoServiceKey CryptoServiceMapping CryptoServiceNeeds CryptoServicePrimitive CryptoServiceQueue CryptoSignatureScheme CryptoTrustMasterInterface CustomCppImplementationDataType DataConstr DataExchangePoint DataFormatElementReference DataFormatElementScope DataInterface DataPrototype DataPrototypeGroup DataReceiveErrorEvent DataReceivedEvent DataSendCompletedEvent DataTransformation DataTransformationSet DataTypeMappingSet DataWriteCompletedEvent DcmIPdu DdsDomainRange DdsEventDeployment DdsFieldDeployment DdsProvidedServiceInstance DdsRequiredServiceInstance DdsSecureComProps DdsSecureGovernance DdsServiceInstanceToMachineMapping DdsServiceInterfaceDeployment DdsTopicAccessRule DeadlineSupervision DefItem DelegationSwConnector DependencyOnArtifact DeterministicClient DeterministicClientResourceNeeds DeterministicSyncInstantiation DeterministicSyncMaster DeterministicSyncMasterToTimeBaseConsumerMapping DevelopmentError DiagEventDebounceAlgorithm DiagEventDebounceCounterBased DiagEventDebounceMonitorInternal DiagEventDebounceTimeBased DiagnosticAbstractAliasEvent DiagnosticAbstractDataIdentifier DiagnosticAbstractDataIdentifierInterface DiagnosticAbstractRoutineInterface DiagnosticAccessPermission DiagnosticAging DiagnosticAuthRole DiagnosticAuthentication DiagnosticAuthenticationClass DiagnosticAuthenticationConfiguration DiagnosticAuthenticationInterface DiagnosticAuthenticationPortMapping DiagnosticCapabilityElement DiagnosticClearCondition DiagnosticClearConditionGroup DiagnosticClearConditionNeeds DiagnosticClearConditionPortMapping DiagnosticClearDiagnosticInformation DiagnosticClearDiagnosticInformationClass DiagnosticClearResetEmissionRelatedInfo DiagnosticClearResetEmissionRelatedInfoClass DiagnosticComControl DiagnosticComControlClass DiagnosticComControlInterface DiagnosticCommonElement DiagnosticCommunicationManagerNeeds DiagnosticComponentNeeds DiagnosticCondition DiagnosticConditionGroup DiagnosticConditionInterface DiagnosticConnectedIndicator DiagnosticConnection DiagnosticContributionSet DiagnosticControlDtcSetting DiagnosticControlDtcSettingClass DiagnosticControlNeeds DiagnosticCustomServiceClass DiagnosticCustomServiceInstance DiagnosticDataByIdentifier DiagnosticDataElement DiagnosticDataElementInterface DiagnosticDataIdentifier DiagnosticDataIdentifierGenericInterface DiagnosticDataIdentifierInterface DiagnosticDataIdentifierSet DiagnosticDataPortMapping DiagnosticDataTransfer DiagnosticDataTransferClass DiagnosticDeAuthentication DiagnosticDebounceAlgorithmProps DiagnosticDemProvidedDataMapping DiagnosticDoIpActivationLineInterface DiagnosticDoIpEntityIdentificationInterface DiagnosticDoIpGroupIdentificationInterface DiagnosticDoIpPowerModeInterface DiagnosticDoIpTriggerVehicleAnnouncementInterface DiagnosticDownloadInterface DiagnosticDtcInformationInterface DiagnosticDynamicDataIdentifier DiagnosticDynamicallyDefineDataIdentifier DiagnosticDynamicallyDefineDataIdentifierClass DiagnosticEcuInstanceProps DiagnosticEcuReset DiagnosticEcuResetClass DiagnosticEcuResetInterface DiagnosticEnableCondition DiagnosticEnableConditionGroup DiagnosticEnableConditionNeeds DiagnosticEnableConditionPortMapping DiagnosticEnvBswModeElement DiagnosticEnvModeElement DiagnosticEnvSwcModeElement DiagnosticEnvironmentalCondition DiagnosticEvent DiagnosticEventInfoNeeds DiagnosticEventInterface DiagnosticEventManagerNeeds DiagnosticEventNeeds DiagnosticEventPortMapping DiagnosticEventToDebounceAlgorithmMapping DiagnosticEventToEnableConditionGroupMapping DiagnosticEventToOperationCycleMapping DiagnosticEventToSecurityEventMapping DiagnosticEventToStorageConditionGroupMapping DiagnosticEventToTroubleCodeJ1939Mapping DiagnosticEventToTroubleCodeUdsMapping DiagnosticExtendedDataRecord DiagnosticExternalAuthenticationInterface DiagnosticExternalAuthenticationPortMapping DiagnosticFimAliasEvent DiagnosticFimAliasEventGroup DiagnosticFimAliasEventGroupMapping DiagnosticFimAliasEventMapping DiagnosticFimEventGroup DiagnosticFimFunctionMapping DiagnosticFreezeFrame DiagnosticFunctionIdentifier DiagnosticFunctionIdentifierInhibit DiagnosticFunctionInhibitSource DiagnosticGenericUdsInterface DiagnosticGenericUdsNeeds DiagnosticIndicator DiagnosticIndicatorInterface DiagnosticIndicatorNeeds DiagnosticIndicatorPortMapping DiagnosticInfoType DiagnosticInhibitSourceEventMapping DiagnosticIoControl DiagnosticIoControlClass DiagnosticIoControlNeeds DiagnosticIumpr DiagnosticIumprDenominatorGroup DiagnosticIumprGroup DiagnosticIumprToFunctionIdentifierMapping DiagnosticJ1939ExpandedFreezeFrame DiagnosticJ1939FreezeFrame DiagnosticJ1939Node DiagnosticJ1939Spn DiagnosticJ1939SpnMapping DiagnosticJ1939SwMapping DiagnosticMapping DiagnosticMasterToSlaveEventMapping DiagnosticMeasurementIdentifier DiagnosticMemoryAddressableRangeAccess DiagnosticMemoryByAddress DiagnosticMemoryDestination DiagnosticMemoryDestinationPortMapping DiagnosticMemoryDestinationPrimary DiagnosticMemoryDestinationUserDefined DiagnosticMemoryIdentifier DiagnosticMonitorInterface DiagnosticMonitorPortMapping DiagnosticOperationCycle DiagnosticOperationCycleInterface DiagnosticOperationCycleNeeds DiagnosticOperationCyclePortMapping DiagnosticParameterElement DiagnosticParameterIdent DiagnosticParameterIdentifier DiagnosticPortInterface DiagnosticPowertrainFreezeFrame DiagnosticProofOfOwnership DiagnosticProtocol DiagnosticProvidedDataMapping DiagnosticReadDataByIdentifier DiagnosticReadDataByIdentifierClass DiagnosticReadDataByPeriodicId DiagnosticReadDataByPeriodicIdClass DiagnosticReadDtcInformation DiagnosticReadDtcInformationClass DiagnosticReadMemoryByAddress DiagnosticReadMemoryByAddressClass DiagnosticReadScalingDataByIdentifier DiagnosticReadScalingDataByIdentifierClass DiagnosticRequestControlOfOnBoardDevice DiagnosticRequestControlOfOnBoardDeviceClass DiagnosticRequestCurrentPowertrainData DiagnosticRequestCurrentPowertrainDataClass DiagnosticRequestDownload DiagnosticRequestDownloadClass DiagnosticRequestEmissionRelatedDtc DiagnosticRequestEmissionRelatedDtcClass DiagnosticRequestEmissionRelatedDtcPermanentStatus DiagnosticRequestEmissionRelatedDtcPermanentStatusClass DiagnosticRequestFileTransfer DiagnosticRequestFileTransferClass DiagnosticRequestFileTransferInterface DiagnosticRequestFileTransferNeeds DiagnosticRequestOnBoardMonitoringTestResults DiagnosticRequestOnBoardMonitoringTestResultsClass DiagnosticRequestPowertrainFreezeFrameData DiagnosticRequestPowertrainFreezeFrameDataClass DiagnosticRequestRoutineResults DiagnosticRequestUpload DiagnosticRequestUploadClass DiagnosticRequestVehicleInfo DiagnosticRequestVehicleInfoClass DiagnosticResponseOnEvent DiagnosticResponseOnEventClass DiagnosticRoutine DiagnosticRoutineControl DiagnosticRoutineControlClass DiagnosticRoutineGenericInterface DiagnosticRoutineInterface DiagnosticRoutineNeeds DiagnosticRoutineSubfunction DiagnosticSecurityAccess DiagnosticSecurityAccessClass DiagnosticSecurityEventReportingModeMapping DiagnosticSecurityLevel DiagnosticSecurityLevelInterface DiagnosticSecurityLevelPortMapping DiagnosticServiceClass DiagnosticServiceDataMapping DiagnosticServiceGenericMapping DiagnosticServiceInstance DiagnosticServiceSwMapping DiagnosticServiceTable DiagnosticServiceValidationInterface DiagnosticServiceValidationMapping DiagnosticSession DiagnosticSessionControl DiagnosticSessionControlClass DiagnosticSovdAuthorizationInterface DiagnosticSovdAuthorizationPortMapping DiagnosticSovdLock DiagnosticSovdPortInterface DiagnosticSovdProximityChallengeInterface DiagnosticSovdProximityChallengePortMapping DiagnosticStartRoutine DiagnosticStopRoutine DiagnosticStorageCondition DiagnosticStorageConditionGroup DiagnosticStorageConditionNeeds DiagnosticStorageConditionPortMapping DiagnosticSwMapping DiagnosticTestResult DiagnosticTestRoutineIdentifier DiagnosticTransferExit DiagnosticTransferExitClass DiagnosticTroubleCode DiagnosticTroubleCodeGroup DiagnosticTroubleCodeJ1939 DiagnosticTroubleCodeObd DiagnosticTroubleCodeProps DiagnosticTroubleCodeUds DiagnosticTroubleCodeUdsToClearConditionGroupMapping DiagnosticTroubleCodeUdsToTroubleCodeObdMapping DiagnosticUploadDownloadNeeds DiagnosticUploadInterface DiagnosticValueNeeds DiagnosticVerifyCertificateBidirectional DiagnosticVerifyCertificateUnidirectional DiagnosticWriteDataByIdentifier DiagnosticWriteDataByIdentifierClass DiagnosticWriteMemoryByAddress DiagnosticWriteMemoryByAddressClass DiagnosticsCommunicationSecurityNeeds DltApplication DltApplicationToProcessMapping DltArgument DltContext DltEcu DltLogChannel DltLogSink DltLogSinkToPortPrototypeMapping DltMessage DltUserNeeds DoIpActivationLineNeeds DoIpGidNeeds DoIpGidSynchronizationNeeds DoIpInstantiation DoIpInterface DoIpLogicAddress DoIpLogicTargetAddressProps DoIpLogicTesterAddressProps DoIpPowerModeStatusNeeds DoIpRoutingActivation DoIpRoutingActivationAuthenticationNeeds DoIpRoutingActivationConfirmationNeeds DoIpServiceNeeds DoIpTpConfig DocumentElementScope Documentation DocumentationContext DtcStatusChangeNotificationNeeds E2EProfileCompatibilityProps E2EProfileConfiguration E2EProfileConfigurationSet EcuAbstractionSwComponentType EcuInstance EcuMapping EcuPartition EcuStateMgrUserNeeds EcuTiming EcucAbstractExternalReferenceDef EcucAbstractInternalReferenceDef EcucAbstractReferenceDef EcucAbstractStringParamDef EcucAddInfoParamDef EcucBooleanParamDef EcucChoiceContainerDef EcucChoiceReferenceDef EcucCommonAttributes EcucContainerDef EcucContainerValue EcucDefinitionCollection EcucDefinitionElement EcucDestinationUriDef EcucDestinationUriDefSet EcucEnumerationLiteralDef EcucEnumerationParamDef EcucFloatParamDef EcucForeignReferenceDef EcucFunctionNameDef EcucInstanceReferenceDef EcucIntegerParamDef EcucLinkerSymbolDef EcucModuleConfigurationValues EcucModuleDef EcucMultilineStringParamDef EcucParamConfContainerDef EcucParameterDef EcucQuery EcucReferenceDef EcucStringParamDef EcucUriReferenceDef EcucValidationCondition EcucValueCollection End2EndEventProtectionProps End2EndMethodProtectionProps EndToEndProtection EndToEndProtectionSet EnumerationMappingTable EocEventRef EocExecutableEntityRef EocExecutableEntityRefAbstract EocExecutableEntityRefGroup ErrorTracerNeeds EthIpProps EthTcpIpIcmpProps EthTcpIpProps EthTpConfig EthernetCluster EthernetCommunicationConnector EthernetCommunicationController EthernetFrameTriggering EthernetPhysicalChannel EthernetPriorityRegeneration EthernetRawDataStreamClientMapping EthernetRawDataStreamGrant EthernetRawDataStreamMapping EthernetRawDataStreamServerMapping EthernetWakeupSleepOnDatalineConfig EthernetWakeupSleepOnDatalineConfigSet EvaluatedVariantSet EventHandler EventMapping EventTriggeringConstraint ExclusiveArea ExclusiveAreaNestingOrder Executable ExecutableEntity ExecutableEntityActivationReason ExecutableTiming ExecutionOrderConstraint ExecutionTime ExecutionTimeConstraint ExternalTriggerOccurredEvent ExternalTriggeringPointIdent FibexElement Field FieldMapping FireAndForgetMethodMapping FirewallRule FirewallStateSwitchInterface FlatInstanceDescriptor FlatMap FlexrayArTpConfig FlexrayArTpNode FlexrayCluster FlexrayCommunicationConnector FlexrayCommunicationController FlexrayFrame FlexrayFrameTriggering FlexrayNmCluster FlexrayNmNode FlexrayPhysicalChannel FlexrayTpConfig FlexrayTpConnectionControl FlexrayTpNode FlexrayTpPduPool FmAttributeDef FmFeature FmFeatureMap FmFeatureMapAssertion FmFeatureMapCondition FmFeatureMapElement FmFeatureModel FmFeatureRelation FmFeatureRestriction FmFeatureSelection FmFeatureSelectionSet Frame FramePort FrameTriggering FunctionGroupSet FunctionInhibitionAvailabilityNeeds FunctionInhibitionNeeds FunctionalClusterInteractsWithFunctionalClusterMapping FunctionalClusterInteractsWithPersistencyDeploymentMapping FurtherActionByteNeeds Gateway GeneralParameter GeneralPurposeConnection GeneralPurposeIPdu GeneralPurposePdu GenericEthernetFrame GenericModuleInstantiation GlobalSupervision GlobalSupervisionNeeds GlobalTimeCanMaster GlobalTimeCanSlave GlobalTimeDomain GlobalTimeEthMaster GlobalTimeEthSlave GlobalTimeFrMaster GlobalTimeFrSlave GlobalTimeGateway GlobalTimeMaster GlobalTimeSlave Grant GrantDesign HardwareTestNeeds HealthChannel HealthChannelExternalStatus HealthChannelSupervision HeapUsage HwAttributeDef HwAttributeLiteralDef HwCategory HwDescriptionEntity HwElement HwPin HwPinGroup HwType IPdu IPduPort IPv6ExtHeaderFilterList IPv6ExtHeaderFilterSet ISignal ISignalGroup ISignalIPdu ISignalIPduGroup ISignalPort ISignalToIPduMapping ISignalTriggering IamModuleInstantiation IdentCaption Identifiable IdsCommonElement IdsDesign IdsMapping IdsMgrCustomTimestampNeeds IdsMgrNeeds IdsPlatformInstantiation IdsmInstance IdsmModuleInstantiation IdsmProperties IdsmRateLimitation IdsmTrafficLimitation Ieee1722TpEthernetFrame Implementation ImplementationDataType ImplementationDataTypeElement ImplementationProps IndicatorStatusNeeds InitEvent InterfaceMapping InternalBehavior InternalTriggerOccurredEvent InternalTriggeringPoint InterpolationRoutineMappingSet IpIamRemoteSubject IpSecConfigProps IpSecIamRemoteSubject IpSecRule J1939Cluster J1939ControllerApplication J1939DcmDm19Support J1939DcmIPdu J1939NmCluster J1939NmNode J1939RmIncomingRequestServiceNeeds J1939RmOutgoingRequestServiceNeeds J1939SharedAddressCluster J1939TpConfig J1939TpNode Keyword KeywordSet LatencyTimingConstraint LifeCycleInfoSet LifeCycleState LifeCycleStateDefinitionGroup LinCluster LinCommunicationConnector LinCommunicationController LinEventTriggeredFrame LinFrame LinFrameTriggering LinMaster LinPhysicalChannel LinScheduleTable LinSlave LinSlaveConfigIdent LinSporadicFrame LinTpConfig LinTpNode LinUnconditionalFrame Linker LogAndTraceInstantiation LogAndTraceInterface LogAndTraceMessageCollectionSet LogicalSupervision LtMessageCollectionToPortPrototypeMapping MacMulticastGroup MacSecGlobalKayProps MacSecKayParticipant MacSecParticipantSet Machine MachineDesign MachineTiming McDataInstance McFunction McGroup MeasuredExecutionTime MeasuredHeapUsage MeasuredStackUsage MemorySection MemoryUsage MethodMapping ModeAccessPointIdent ModeDeclaration ModeDeclarationGroup ModeDeclarationGroupPrototype ModeDeclarationMapping ModeDeclarationMappingSet ModeInterfaceMapping ModeSwitchInterface ModeSwitchPoint ModeSwitchedAckEvent ModeTransition MultilanguageReferrable MultiplexedIPdu NPdu NetworkEndpoint NmCluster NmConfig NmEcu NmHandleToFunctionGroupStateMapping NmInstantiation NmNetworkHandle NmNode NmPdu NoCheckpointSupervision NoSupervision NonOsModuleInstantiation NvBlockDescriptor NvBlockNeeds NvBlockSwComponentType NvDataInterface ObdControlServiceNeeds ObdInfoServiceNeeds ObdMonitorServiceNeeds ObdPidServiceNeeds ObdRatioDenominatorNeeds ObdRatioServiceNeeds OffsetTimingConstraint OperationInvokedEvent OsModuleInstantiation OsTaskExecutionEvent OsTaskProxy PPortPrototype PackageableElement ParameterAccess ParameterDataPrototype ParameterInterface ParameterSwComponentType PassThroughSwConnector Pdu PduActivationRoutingGroup PduToFrameMapping PduTriggering PdurIPduGroup PerInstanceMemory PeriodicEventTriggering PersistencyDataElement PersistencyDeployment PersistencyDeploymentElement PersistencyDeploymentElementToCryptoKeySlotMapping PersistencyDeploymentToCryptoKeySlotMapping PersistencyDeploymentToDltLogSinkMapping PersistencyFile PersistencyFileElement PersistencyFileStorage PersistencyFileStorageInterface PersistencyInterface PersistencyInterfaceElement PersistencyKeyValuePair PersistencyKeyValueStorage PersistencyKeyValueStorageInterface PersistencyPortPrototypeToDeploymentMapping PersistencyPortPrototypeToFileStorageMapping PersistencyPortPrototypeToKeyValueStorageMapping PhmAbstractRecoveryNotificationInterface PhmCheckpoint PhmContributionToMachineMapping PhmHealthChannelInterface PhmHealthChannelRecoveryNotificationInterface PhmHealthChannelStatus PhmRecoveryActionInterface PhmSupervisedEntityInterface PhmSupervision PhmSupervisionRecoveryNotificationInterface PhysicalChannel PhysicalDimension PhysicalDimensionMappingSet PlatformHealthManagementContribution PlatformHealthManagementInterface PlatformModuleEndpointConfiguration PlatformModuleEthernetEndpointConfiguration PncMappingIdent PortElementToCommunicationResourceMapping PortGroup PortInterface PortInterfaceMapping PortInterfaceMappingSet PortInterfaceToDataTypeMapping PortPrototype PortPrototypeBlueprint PossibleErrorReaction PostBuildVariantCriterion PostBuildVariantCriterionValueSet PrPortPrototype PredefinedVariant PrimitiveAttributeTailoring Process ProcessDesign ProcessDesignToMachineDesignMapping ProcessExecutionError ProcessToMachineMapping ProcessToMachineMappingSet Processor ProcessorCore ProvidedApServiceInstance ProvidedServiceInstance ProvidedServiceInstanceToSwClusterDesignPPortPrototypeMapping ProvidedSomeipServiceInstance ProvidedUserDefinedServiceInstance PskIdentityToKeySlotMapping RPortPrototype RapidPrototypingScenario RawDataStreamClientInterface RawDataStreamDeployment RawDataStreamGrant RawDataStreamGrantDesign RawDataStreamMapping RawDataStreamServerInterface RecoveryNotification RecoveryNotificationToPPortPrototypeMapping ReferenceTailoring Referrable RequiredApServiceInstance RequiredServiceInstanceToSwClusterDesignRPortPrototypeMapping RequiredSomeipServiceInstance RequiredUserDefinedServiceInstance ResourceConsumption ResourceGroup RootSwClusterDesignComponentPrototype RootSwComponentPrototype RootSwCompositionPrototype RoughEstimateHeapUsage RoughEstimateOfExecutionTime RoughEstimateStackUsage RptComponent RptContainer RptExecutableEntity RptExecutableEntityEvent RptExecutionContext RptProfile RptServicePoint RteEvent RteEventInCompositionSeparation RteEventInCompositionToOsTaskProxyMapping RteEventInSystemSeparation RteEventInSystemToOsTaskProxyMapping RunnableEntity RunnableEntityGroup RuntimeError SdgAbstractForeignReference SdgAbstractPrimitiveAttribute SdgAggregationWithVariation SdgAttribute SdgCaption SdgClass SdgDef SdgForeignReference SdgForeignReferenceWithVariation SdgPrimitiveAttribute SdgPrimitiveAttributeWithVariation SdgReference SdgTailoring SecOcCryptoServiceMapping SecOcDeployment SecOcJobMapping SecOcJobRequirement SecOcSecureComProps SectionNamePrefix SecureComProps SecureCommunicationAuthenticationProps SecureCommunicationDeployment SecureCommunicationFreshnessProps SecureCommunicationPropsSet SecureOnBoardCommunicationNeeds SecuredIPdu SecurityEventAggregationFilter SecurityEventContextMapping SecurityEventContextMappingApplication SecurityEventContextMappingBswModule SecurityEventContextMappingCommConnector SecurityEventContextMappingFunctionalCluster SecurityEventContextProps SecurityEventDefinition SecurityEventFilterChain SecurityEventMapping SecurityEventOneEveryNFilter SecurityEventReportInterface SecurityEventReportToSecurityEventDefinitionMapping SecurityEventStateFilter SecurityEventThresholdFilter SenderReceiverInterface SensorActuatorSwComponentType ServerCallPoint ServiceEventDeployment ServiceFieldDeployment ServiceInstanceCollectionSet ServiceInstanceToMachineMapping ServiceInstanceToPortPrototypeMapping ServiceInstanceToSignalMapping ServiceInstanceToSwClusterDesignPortPrototypeMapping ServiceInterface ServiceInterfaceDeployment ServiceInterfaceElementMapping ServiceInterfaceElementSecureComConfig ServiceInterfaceEventMapping ServiceInterfaceFieldMapping ServiceInterfaceMapping ServiceInterfaceMethodMapping ServiceInterfacePedigree ServiceInterfaceTriggerMapping ServiceMethodDeployment ServiceNeeds ServiceProxySwComponentType ServiceSwComponentType ServiceTiming SignalBasedEventElementToISignalTriggeringMapping SignalBasedFieldToISignalTriggeringMapping SignalBasedFireAndForgetMethodToISignalTriggeringMapping SignalBasedMethodToISignalTriggeringMapping SignalBasedTriggerToISignalTriggeringMapping SignalServiceTranslationElementProps SignalServiceTranslationEventProps SignalServiceTranslationProps SignalServiceTranslationPropsSet SimulatedExecutionTime SingleLanguageReferrable SoAdRoutingGroup SoConIPduIdentifier SocketAddress SocketConnectionBundle SocketConnectionIpduIdentifierSet SoftwareCluster SoftwareClusterDesign SoftwareClusterDiagnosticDeploymentProps SoftwarePackage SoftwarePackageStep SomeipDataPrototypeTransformationProps SomeipEventDeployment SomeipEventGroup SomeipFieldDeployment SomeipMethodDeployment SomeipProvidedEventGroup SomeipRemoteMulticastConfig SomeipRemoteUnicastConfig SomeipRequiredEventGroup SomeipSdClientEventGroupTimingConfig SomeipSdClientServiceInstanceConfig SomeipSdServerEventGroupTimingConfig SomeipSdServerServiceInstanceConfig SomeipServiceInstanceToMachineMapping SomeipServiceInterfaceDeployment SomeipTpChannel SomeipTpConfig SomeipTransformationProps SovdGatewayInstantiation SovdModuleInstantiation SovdServerInstantiation SpecElementReference SpecElementScope SpecificationDocumentScope SporadicEventTriggering StackUsage StartupConfig StateDependentFirewall StateManagemenPhmErrorInterface StateManagementActionItem StateManagementActionList StateManagementDiagTriggerInterface StateManagementEmErrorInterface StateManagementErrorInterface StateManagementFunctionGroupSwitchNotificationInterface StateManagementModuleInstantiation StateManagementNotificationInterface StateManagementPortInterface StateManagementRequestError StateManagementRequestInterface StateManagementRequestTrigger StateManagementSetFunctionGroupStateActionItem StateManagementStateMachineActionItem StateManagementStateNotification StateManagementStateRequest StateManagementSyncActionItem StateManagementTriggerInterface StaticSocketConnection Std StdCppImplementationDataType StructuredReq SupervisedEntityCheckpointNeeds SupervisedEntityNeeds SupervisionCheckpoint SupervisionMode SupervisionModeCondition SwAddrMethod SwAxisType SwBaseType SwComponentMappingConstraints SwComponentPrototype SwComponentType SwConnector SwGenericAxisParamType SwRecordLayout SwServiceArg SwSystemconst SwSystemconstantValueSet SwcBswMapping SwcImplementation SwcInternalBehavior SwcModeManagerErrorEvent SwcModeSwitchEvent SwcServiceDependency SwcTiming SwcToApplicationPartitionMapping SwcToEcuMapping SwcToImplMapping SymbolProps SymbolicNameProps SyncTimeBaseMgrUserNeeds SynchronizationPointConstraint SynchronizationTimingConstraint SynchronizedTimeBaseConsumer SynchronizedTimeBaseConsumerInterface SynchronizedTimeBaseProvider SynchronizedTimeBaseProviderInterface SynchronousServerCallPoint System SystemMapping SystemSignal SystemSignalGroup SystemTiming TcpOptionFilterList TcpOptionFilterSet TdCpSoftwareClusterMapping TdCpSoftwareClusterMappingSet TdCpSoftwareClusterResourceMapping TdEventBsw TdEventBswInternalBehavior TdEventBswModeDeclaration TdEventBswModule TdEventCom TdEventComplex TdEventCycleStart TdEventFrClusterCycleStart TdEventFrame TdEventFrameEthernet TdEventIPdu TdEventISignal TdEventModeDeclaration TdEventOperation TdEventServiceInstance TdEventServiceInstanceDiscovery TdEventServiceInstanceEvent TdEventServiceInstanceField TdEventServiceInstanceMethod TdEventSllet TdEventSlletPort TdEventSwc TdEventSwcInternalBehavior TdEventSwcInternalBehaviorReference TdEventTrigger TdEventTtCanCycleStart TdEventVariableDataPrototype TdEventVfb TdEventVfbPort TdEventVfbReference TdletZoneClock TimeBaseProviderToPersistencyMapping TimeBaseResource TimeSyncModuleInstantiation TimeSyncPortPrototypeToTimeBaseMapping TimeSyncServerConfiguration TimingClock TimingClockSyncAccuracy TimingCondition TimingConstraint TimingDescription TimingDescriptionEvent TimingDescriptionEventChain TimingEvent TimingExtension TimingExtensionResource TimingModeInstance TlsConnectionGroup TlsCryptoCipherSuite TlsCryptoCipherSuiteProps TlsCryptoServiceMapping TlsDeployment TlsIamRemoteSubject TlsJobMapping TlsSecureComProps TlvDataIdDefinitionSet Topic1 TpAddress TpConfig TpConnectionIdent Traceable TraceableTable TraceableText TracedFailure TransformationProps TransformationPropsSet TransformationPropsToServiceInterfaceElementMapping TransformationTechnology TransformerHardErrorEvent TransientFault Trigger TriggerInterface TriggerInterfaceMapping TtcanCluster TtcanCommunicationConnector TtcanCommunicationController TtcanPhysicalChannel UcmDescription UcmMasterModuleInstantiation UcmModuleInstantiation UcmRetryStrategy UcmStep UcmSubordinateModuleInstantiation UcmToTimeBaseResourceMapping UdpNmCluster UdpNmNode Unit UnitGroup UploadableExclusivePackageElement UploadablePackageElement UserDefinedCluster UserDefinedCommunicationConnector UserDefinedCommunicationController UserDefinedEthernetFrame UserDefinedEventDeployment UserDefinedFieldDeployment UserDefinedGlobalTimeMaster UserDefinedGlobalTimeSlave UserDefinedIPdu UserDefinedMethodDeployment UserDefinedPdu UserDefinedPhysicalChannel UserDefinedServiceInstanceToMachineMapping UserDefinedServiceInterfaceDeployment UserDefinedTransformationProps V2XDataManagerNeeds V2XFacUserNeeds V2XMUserNeeds VariableAccess VariableAndParameterInterfaceMapping VariableDataPrototype VariationPointProxy VehiclePackage VehicleRolloutStep VendorSpecificServiceNeeds VfbTiming ViewMap ViewMapSet VlanConfig WaitPoint WarningIndicatorRequestedBitNeeds WorstCaseHeapUsage WorstCaseStackUsage Xdoc Xfile XrefTarget """.split()


#------------------------------------------------------------------------------
# Class FullBindingTimeEnum
#------------------------------------------------------------------------------
class FullBindingTimeEnum(ENUM):
	"""Defines FullBindingTimeEnum Enums"""
	_names_ = """undefined BlueprintDerivationTime CodeGenerationTime LinkTime PostBuild PreCompileTime SystemDesignTime """.split()


#------------------------------------------------------------------------------
# Class StandardNameEnum
#------------------------------------------------------------------------------
class StandardNameEnum(ENUM):
	"""Defines StandardNameEnum Enums"""
	_names_ = """undefined Ap Cp Fo Ta Tc """.split()


#------------------------------------------------------------------------------
# Class FMFeatureSelectionStateEnum
#------------------------------------------------------------------------------
class FMFeatureSelectionStateEnum(ENUM):
	"""Defines FMFeatureSelectionStateEnum Enums"""
	_names_ = """undefined Deselected Selected Undecided """.split()


#------------------------------------------------------------------------------
# Class EcucConfigurationClassEnum
#------------------------------------------------------------------------------
class EcucConfigurationClassEnum(ENUM):
	"""Defines EcucConfigurationClassEnum Enums"""
	_names_ = """undefined Link PostBuild PreCompile PublishedInformation """.split()


#------------------------------------------------------------------------------
# Class EcucConfigurationVariantEnum
#------------------------------------------------------------------------------
class EcucConfigurationVariantEnum(ENUM):
	"""Defines EcucConfigurationVariantEnum Enums"""
	_names_ = """undefined PreconfiguredConfiguration RecommendedConfiguration VariantLinkTime VariantPostBuild VariantPreCompile """.split()


#------------------------------------------------------------------------------
# Class EcucDestinationUriNestingContractEnum
#------------------------------------------------------------------------------
class EcucDestinationUriNestingContractEnum(ENUM):
	"""Defines EcucDestinationUriNestingContractEnum Enums"""
	_names_ = """undefined LeafOfTargetContainer TargetContainer VertexOfTargetContainer """.split()


#------------------------------------------------------------------------------
# Class EcucScopeEnum
#------------------------------------------------------------------------------
class EcucScopeEnum(ENUM):
	"""Defines EcucScopeEnum Enums"""
	_names_ = """undefined Ecu Local """.split()


#------------------------------------------------------------------------------
# Class EEnum
#------------------------------------------------------------------------------
class EEnum(ENUM):
	"""Defines EEnum Enums"""
	_names_ = """undefined Bold Bolditalic Italic Plain """.split()


#------------------------------------------------------------------------------
# Class EEnumFontEnum
#------------------------------------------------------------------------------
class EEnumFontEnum(ENUM):
	"""Defines EEnumFontEnum Enums"""
	_names_ = """undefined Default Mono """.split()


#------------------------------------------------------------------------------
# Class LEnum
#------------------------------------------------------------------------------
class LEnum(ENUM):
	"""Defines LEnum Enums"""
	_names_ = """Aa Ab Af Am Ar As Ay Az Ba Be Bg Bh Bi Bn Bo Br Ca Co Cs Cy Da De Dz El En Eo Es Et Eu Fa Fi Fj Fo ForAll Fr Fy Ga Gd Gl Gn Gu Ha Hi Hr Hu Hy Ia Ie Ik In Is It Iw Ja Ji Jw Ka Kk Kl Km Kn Ko Ks Ku Ky La Ln Lo Lt Lv Mg Mi Mk Ml Mn Mo Mr Ms Mt My Na Ne Nl No Oc Om Or Pa Pl Ps Pt Qu Rm Rn Ro Ru Rw Sa Sd Sg Sh Si Sk Sl Sm Sn So Sq Sr Ss St Su Sv Sw Ta Te Tg Th Ti Tk Tl Tn To Tr Ts Tt Tw Uk Ur Uz Vi Vo Wo Xh Yo Zh Zu """.split()


#------------------------------------------------------------------------------
# Class LUndefinedEnum
#------------------------------------------------------------------------------
class LUndefinedEnum(ENUM):
	"""Defines LUndefinedEnum Enums"""
	_names_ = """undefined Aa Ab Af Am Ar As Ay Az Ba Be Bg Bh Bi Bn Bo Br Ca Co Cs Cy Da De Dz El En Eo Es Et Eu Fa Fi Fj Fo ForAll Fr Fy Ga Gd Gl Gn Gu Ha Hi Hr Hu Hy Ia Ie Ik In Is It Iw Ja Ji Jw Ka Kk Kl Km Kn Ko Ks Ku Ky La Ln Lo Lt Lv Mg Mi Mk Ml Mn Mo Mr Ms Mt My Na Ne Nl No Oc Om Or Pa Pl Ps Pt Qu Rm Rn Ro Ru Rw Sa Sd Sg Sh Si Sk Sl Sm Sn So Sq Sr Ss St Su Sv Sw Ta Te Tg Th Ti Tk Tl Tn To Tr Ts Tt Tw Uk Ur Uz Vi Vo Wo Xh Yo Zh Zu """.split()


#------------------------------------------------------------------------------
# Class ResolutionPolicyEnum
#------------------------------------------------------------------------------
class ResolutionPolicyEnum(ENUM):
	"""Defines ResolutionPolicyEnum Enums"""
	_names_ = """undefined NoSloppy Sloppy """.split()


#------------------------------------------------------------------------------
# Class ShowContentEnum
#------------------------------------------------------------------------------
class ShowContentEnum(ENUM):
	"""Defines ShowContentEnum Enums"""
	_names_ = """undefined NoShowContent ShowContent """.split()


#------------------------------------------------------------------------------
# Class ShowResourceAliasNameEnum
#------------------------------------------------------------------------------
class ShowResourceAliasNameEnum(ENUM):
	"""Defines ShowResourceAliasNameEnum Enums"""
	_names_ = """undefined NoShowAliasName ShowAliasName """.split()


#------------------------------------------------------------------------------
# Class ShowResourceCategoryEnum
#------------------------------------------------------------------------------
class ShowResourceCategoryEnum(ENUM):
	"""Defines ShowResourceCategoryEnum Enums"""
	_names_ = """undefined NoShowCategory ShowCategory """.split()


#------------------------------------------------------------------------------
# Class ShowResourceLongNameEnum
#------------------------------------------------------------------------------
class ShowResourceLongNameEnum(ENUM):
	"""Defines ShowResourceLongNameEnum Enums"""
	_names_ = """undefined NoShowLongName ShowLongName """.split()


#------------------------------------------------------------------------------
# Class ShowResourceNumberEnum
#------------------------------------------------------------------------------
class ShowResourceNumberEnum(ENUM):
	"""Defines ShowResourceNumberEnum Enums"""
	_names_ = """undefined NoShowNumber ShowNumber """.split()


#------------------------------------------------------------------------------
# Class ShowResourcePageEnum
#------------------------------------------------------------------------------
class ShowResourcePageEnum(ENUM):
	"""Defines ShowResourcePageEnum Enums"""
	_names_ = """undefined NoShowPage ShowPage """.split()


#------------------------------------------------------------------------------
# Class ShowResourceShortNameEnum
#------------------------------------------------------------------------------
class ShowResourceShortNameEnum(ENUM):
	"""Defines ShowResourceShortNameEnum Enums"""
	_names_ = """undefined NoShowShortName ShowShortName """.split()


#------------------------------------------------------------------------------
# Class ShowResourceTypeEnum
#------------------------------------------------------------------------------
class ShowResourceTypeEnum(ENUM):
	"""Defines ShowResourceTypeEnum Enums"""
	_names_ = """undefined NoShowType ShowType """.split()


#------------------------------------------------------------------------------
# Class ShowSeeEnum
#------------------------------------------------------------------------------
class ShowSeeEnum(ENUM):
	"""Defines ShowSeeEnum Enums"""
	_names_ = """undefined NoShowSee ShowSee """.split()


#------------------------------------------------------------------------------
# Class AlignEnum
#------------------------------------------------------------------------------
class AlignEnum(ENUM):
	"""Defines AlignEnum Enums"""
	_names_ = """undefined Center Justify Left Right """.split()


#------------------------------------------------------------------------------
# Class AreaEnumNohrefEnum
#------------------------------------------------------------------------------
class AreaEnumNohrefEnum(ENUM):
	"""Defines AreaEnumNohrefEnum Enums"""
	_names_ = """undefined Nohref """.split()


#------------------------------------------------------------------------------
# Class AreaEnumShapeEnum
#------------------------------------------------------------------------------
class AreaEnumShapeEnum(ENUM):
	"""Defines AreaEnumShapeEnum Enums"""
	_names_ = """undefined Circle Default Poly Rect """.split()


#------------------------------------------------------------------------------
# Class ChapterEnumBreakEnum
#------------------------------------------------------------------------------
class ChapterEnumBreakEnum(ENUM):
	"""Defines ChapterEnumBreakEnum Enums"""
	_names_ = """undefined Break NoBreak """.split()


#------------------------------------------------------------------------------
# Class FloatEnum
#------------------------------------------------------------------------------
class FloatEnum(ENUM):
	"""Defines FloatEnum Enums"""
	_names_ = """undefined Float NoFloat """.split()


#------------------------------------------------------------------------------
# Class FrameEnum
#------------------------------------------------------------------------------
class FrameEnum(ENUM):
	"""Defines FrameEnum Enums"""
	_names_ = """undefined All Bottom NONE Sides Top Topbot """.split()


#------------------------------------------------------------------------------
# Class GraphicFitEnum
#------------------------------------------------------------------------------
class GraphicFitEnum(ENUM):
	"""Defines GraphicFitEnum Enums"""
	_names_ = """undefined AsIs FitToPage FitToText LimitToPage LimitToText Rotate180 Rotate180LimitToText Rotate90Ccw Rotate90CcwFitToText Rotate90CcwLimitToText Rotate90Cw Rotate90CwFitToText Rotate90CwLimitToText """.split()


#------------------------------------------------------------------------------
# Class GraphicNotationEnum
#------------------------------------------------------------------------------
class GraphicNotationEnum(ENUM):
	"""Defines GraphicNotationEnum Enums"""
	_names_ = """undefined Bmp Eps Gif Jpg Pdf Png Svg Tiff """.split()


#------------------------------------------------------------------------------
# Class ItemLabelPosEnum
#------------------------------------------------------------------------------
class ItemLabelPosEnum(ENUM):
	"""Defines ItemLabelPosEnum Enums"""
	_names_ = """undefined Newline NewlineIfNecessary NoNewline """.split()


#------------------------------------------------------------------------------
# Class KeepWithPreviousEnum
#------------------------------------------------------------------------------
class KeepWithPreviousEnum(ENUM):
	"""Defines KeepWithPreviousEnum Enums"""
	_names_ = """undefined Keep NoKeep """.split()


#------------------------------------------------------------------------------
# Class ListEnum
#------------------------------------------------------------------------------
class ListEnum(ENUM):
	"""Defines ListEnum Enums"""
	_names_ = """undefined Number Unnumber """.split()


#------------------------------------------------------------------------------
# Class NoteTypeEnum
#------------------------------------------------------------------------------
class NoteTypeEnum(ENUM):
	"""Defines NoteTypeEnum Enums"""
	_names_ = """undefined Caution Example Exercise Hint Instruction Other Tip """.split()


#------------------------------------------------------------------------------
# Class OrientEnum
#------------------------------------------------------------------------------
class OrientEnum(ENUM):
	"""Defines OrientEnum Enums"""
	_names_ = """undefined Land Port """.split()


#------------------------------------------------------------------------------
# Class PgwideEnum
#------------------------------------------------------------------------------
class PgwideEnum(ENUM):
	"""Defines PgwideEnum Enums"""
	_names_ = """undefined NoPgwide Pgwide """.split()


#------------------------------------------------------------------------------
# Class ValignEnum
#------------------------------------------------------------------------------
class ValignEnum(ENUM):
	"""Defines ValignEnum Enums"""
	_names_ = """undefined Bottom Middle Top """.split()


#------------------------------------------------------------------------------
# Class DiagnosticInhibitionMaskEnum
#------------------------------------------------------------------------------
class DiagnosticInhibitionMaskEnum(ENUM):
	"""Defines DiagnosticInhibitionMaskEnum Enums"""
	_names_ = """undefined LastFailed NotTested Tested TestedAndFailed """.split()


#------------------------------------------------------------------------------
# Class DiagnosticObdSupportEnum
#------------------------------------------------------------------------------
class DiagnosticObdSupportEnum(ENUM):
	"""Defines DiagnosticObdSupportEnum Enums"""
	_names_ = """undefined MasterEcu NoObdSupport PrimaryEcu SecondaryEcu """.split()


#------------------------------------------------------------------------------
# Class DiagnosticClearDtcLimitationEnum
#------------------------------------------------------------------------------
class DiagnosticClearDtcLimitationEnum(ENUM):
	"""Defines DiagnosticClearDtcLimitationEnum Enums"""
	_names_ = """undefined AllSupportedDtcs ClearAllDtcs """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventCombinationBehaviorEnum
#------------------------------------------------------------------------------
class DiagnosticEventCombinationBehaviorEnum(ENUM):
	"""Defines DiagnosticEventCombinationBehaviorEnum Enums"""
	_names_ = """undefined EventCombinationOnRetrieval EventCombinationOnStorage """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventCombinationReportingBehaviorEnum
#------------------------------------------------------------------------------
class DiagnosticEventCombinationReportingBehaviorEnum(ENUM):
	"""Defines DiagnosticEventCombinationReportingBehaviorEnum Enums"""
	_names_ = """undefined ReportingInChronlogicalOrderOldestFirst """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventDisplacementStrategyEnum
#------------------------------------------------------------------------------
class DiagnosticEventDisplacementStrategyEnum(ENUM):
	"""Defines DiagnosticEventDisplacementStrategyEnum Enums"""
	_names_ = """undefined Full NONE PrioOcc """.split()


#------------------------------------------------------------------------------
# Class DiagnosticMemoryEntryStorageTriggerEnum
#------------------------------------------------------------------------------
class DiagnosticMemoryEntryStorageTriggerEnum(ENUM):
	"""Defines DiagnosticMemoryEntryStorageTriggerEnum Enums"""
	_names_ = """undefined Confirmed FdcThreshold TestFailed """.split()


#------------------------------------------------------------------------------
# Class DiagnosticOccurrenceCounterProcessingEnum
#------------------------------------------------------------------------------
class DiagnosticOccurrenceCounterProcessingEnum(ENUM):
	"""Defines DiagnosticOccurrenceCounterProcessingEnum Enums"""
	_names_ = """undefined ConfirmedDtcBit TestFailedBit """.split()


#------------------------------------------------------------------------------
# Class DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum
#------------------------------------------------------------------------------
class DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum(ENUM):
	"""Defines DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum Enums"""
	_names_ = """undefined StatusBitAgingAndDisplacement StatusBitNormal """.split()


#------------------------------------------------------------------------------
# Class DiagnosticTypeOfDtcSupportedEnum
#------------------------------------------------------------------------------
class DiagnosticTypeOfDtcSupportedEnum(ENUM):
	"""Defines DiagnosticTypeOfDtcSupportedEnum Enums"""
	_names_ = """undefined Iso119924 Iso142291 Iso150316 SaeJ193973 SaeJ2012Da """.split()


#------------------------------------------------------------------------------
# Class DiagnosticTypeOfFreezeFrameRecordNumerationEnum
#------------------------------------------------------------------------------
class DiagnosticTypeOfFreezeFrameRecordNumerationEnum(ENUM):
	"""Defines DiagnosticTypeOfFreezeFrameRecordNumerationEnum Enums"""
	_names_ = """undefined Calculated Configured """.split()


#------------------------------------------------------------------------------
# Class DiagnosticSignificanceEnum
#------------------------------------------------------------------------------
class DiagnosticSignificanceEnum(ENUM):
	"""Defines DiagnosticSignificanceEnum Enums"""
	_names_ = """undefined Fault Occurence """.split()


#------------------------------------------------------------------------------
# Class DiagnosticTroubleCodeJ1939DtcKindEnum
#------------------------------------------------------------------------------
class DiagnosticTroubleCodeJ1939DtcKindEnum(ENUM):
	"""Defines DiagnosticTroubleCodeJ1939DtcKindEnum Enums"""
	_names_ = """undefined ServiceOnly Standard """.split()


#------------------------------------------------------------------------------
# Class DiagnosticUdsSeverityEnum
#------------------------------------------------------------------------------
class DiagnosticUdsSeverityEnum(ENUM):
	"""Defines DiagnosticUdsSeverityEnum Enums"""
	_names_ = """undefined CheckAtNextHalt Immediately MaintenanceOnly NoSeverity """.split()


#------------------------------------------------------------------------------
# Class DiagnosticOperationCycleTypeEnum
#------------------------------------------------------------------------------
class DiagnosticOperationCycleTypeEnum(ENUM):
	"""Defines DiagnosticOperationCycleTypeEnum Enums"""
	_names_ = """undefined Ignition ObdDrivingCycle Other Warmup """.split()


#------------------------------------------------------------------------------
# Class DiagnosticIndicatorTypeEnum
#------------------------------------------------------------------------------
class DiagnosticIndicatorTypeEnum(ENUM):
	"""Defines DiagnosticIndicatorTypeEnum Enums"""
	_names_ = """undefined AmberWarning Malfunction ProtectLamp RedStopLamp Warning """.split()


#------------------------------------------------------------------------------
# Class DiagnosticRecordTriggerEnum
#------------------------------------------------------------------------------
class DiagnosticRecordTriggerEnum(ENUM):
	"""Defines DiagnosticRecordTriggerEnum Enums"""
	_names_ = """undefined Confirmed Custom FdcThreshold Pending TestFailed TestFailedThisOperationCycle TestPassed """.split()


#------------------------------------------------------------------------------
# Class DiagnosticClearEventAllowedBehaviorEnum
#------------------------------------------------------------------------------
class DiagnosticClearEventAllowedBehaviorEnum(ENUM):
	"""Defines DiagnosticClearEventAllowedBehaviorEnum Enums"""
	_names_ = """undefined NoStatusByteChange OnlyThisCycleAndReadiness """.split()


#------------------------------------------------------------------------------
# Class DiagnosticConnectedIndicatorBehaviorEnum
#------------------------------------------------------------------------------
class DiagnosticConnectedIndicatorBehaviorEnum(ENUM):
	"""Defines DiagnosticConnectedIndicatorBehaviorEnum Enums"""
	_names_ = """undefined BlinkMode BlinkOrContinuousOnMode ContinuousOnMode FastFlashingMode SlowFlashingMode """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventClearAllowedEnum
#------------------------------------------------------------------------------
class DiagnosticEventClearAllowedEnum(ENUM):
	"""Defines DiagnosticEventClearAllowedEnum Enums"""
	_names_ = """undefined Always RequiresCallbackExecution """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventKindEnum
#------------------------------------------------------------------------------
class DiagnosticEventKindEnum(ENUM):
	"""Defines DiagnosticEventKindEnum Enums"""
	_names_ = """undefined Bsw Swc """.split()


#------------------------------------------------------------------------------
# Class DiagnosticIumprKindEnum
#------------------------------------------------------------------------------
class DiagnosticIumprKindEnum(ENUM):
	"""Defines DiagnosticIumprKindEnum Enums"""
	_names_ = """undefined ApiBased ObserverBased """.split()


#------------------------------------------------------------------------------
# Class DiagnosticJumpToBootLoaderEnum
#------------------------------------------------------------------------------
class DiagnosticJumpToBootLoaderEnum(ENUM):
	"""Defines DiagnosticJumpToBootLoaderEnum Enums"""
	_names_ = """undefined NoBoot OemBoot OemBootRespApp SystemSupplierBoot SystemSupplierBootRespApp """.split()


#------------------------------------------------------------------------------
# Class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum
#------------------------------------------------------------------------------
class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(ENUM):
	"""Defines DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum Enums"""
	_names_ = """undefined ClearDynamicallyDefineDataIdentifier DefineByIdentifier DefineByMemoryAddress """.split()


#------------------------------------------------------------------------------
# Class DiagnosticHandleDDDIConfigurationEnum
#------------------------------------------------------------------------------
class DiagnosticHandleDDDIConfigurationEnum(ENUM):
	"""Defines DiagnosticHandleDDDIConfigurationEnum Enums"""
	_names_ = """undefined NonVolatile Volatile """.split()


#------------------------------------------------------------------------------
# Class DiagnosticEventWindowTimeEnum
#------------------------------------------------------------------------------
class DiagnosticEventWindowTimeEnum(ENUM):
	"""Defines DiagnosticEventWindowTimeEnum Enums"""
	_names_ = """undefined InfiniteTimeToResponse PowerWindowTime """.split()


#------------------------------------------------------------------------------
# Class DiagnosticResponseOnEventActionEnum
#------------------------------------------------------------------------------
class DiagnosticResponseOnEventActionEnum(ENUM):
	"""Defines DiagnosticResponseOnEventActionEnum Enums"""
	_names_ = """undefined Clear OnChangeOfDataIdentifier OnComparisonOfValues OnDtcStatusChange Report ReportDtcRecordInformationOnDtcStatusChange ReportMostRecentDtcOnStatusChange Start Stop """.split()


#------------------------------------------------------------------------------
# Class DiagnosticPeriodicRateCategoryEnum
#------------------------------------------------------------------------------
class DiagnosticPeriodicRateCategoryEnum(ENUM):
	"""Defines DiagnosticPeriodicRateCategoryEnum Enums"""
	_names_ = """undefined PeriodicRateFast PeriodicRateMedium PeriodicRateSlow """.split()


#------------------------------------------------------------------------------
# Class DiagnosticCompareTypeEnum
#------------------------------------------------------------------------------
class DiagnosticCompareTypeEnum(ENUM):
	"""Defines DiagnosticCompareTypeEnum Enums"""
	_names_ = """undefined IsEqual IsGreaterOrEqual IsGreaterThan IsLessOrEqual IsLessThan IsNotEqual """.split()


#------------------------------------------------------------------------------
# Class DiagnosticLogicalOperatorEnum
#------------------------------------------------------------------------------
class DiagnosticLogicalOperatorEnum(ENUM):
	"""Defines DiagnosticLogicalOperatorEnum Enums"""
	_names_ = """undefined LogicalAnd LogicalOr """.split()


#------------------------------------------------------------------------------
# Class DiagnosticResponseToEcuResetEnum
#------------------------------------------------------------------------------
class DiagnosticResponseToEcuResetEnum(ENUM):
	"""Defines DiagnosticResponseToEcuResetEnum Enums"""
	_names_ = """undefined RespondAfterReset RespondBeforeReset """.split()


#------------------------------------------------------------------------------
# Class CalprmAxisCategoryEnum
#------------------------------------------------------------------------------
class CalprmAxisCategoryEnum(ENUM):
	"""Defines CalprmAxisCategoryEnum Enums"""
	_names_ = """undefined Com_axis Fix_axis Res_axis Std_axis """.split()


#------------------------------------------------------------------------------
# Class MemoryAllocationKeywordPolicyTypeEnum
#------------------------------------------------------------------------------
class MemoryAllocationKeywordPolicyTypeEnum(ENUM):
	"""Defines MemoryAllocationKeywordPolicyTypeEnum Enums"""
	_names_ = """undefined AddrMethodShortName AddrMethodShortNameAndAlignment """.split()


#------------------------------------------------------------------------------
# Class MemorySectionTypeEnum
#------------------------------------------------------------------------------
class MemorySectionTypeEnum(ENUM):
	"""Defines MemorySectionTypeEnum Enums"""
	_names_ = """undefined CalibrationVariables Calprm Code ConfigData Const ExcludeFromFlash Var """.split()


#------------------------------------------------------------------------------
# Class SwCalibrationAccessEnum
#------------------------------------------------------------------------------
class SwCalibrationAccessEnum(ENUM):
	"""Defines SwCalibrationAccessEnum Enums"""
	_names_ = """undefined NotAccessible ReadOnly ReadWrite """.split()


#------------------------------------------------------------------------------
# Class SwImplPolicyEnum
#------------------------------------------------------------------------------
class SwImplPolicyEnum(ENUM):
	"""Defines SwImplPolicyEnum Enums"""
	_names_ = """undefined Const Fixed MeasurementPoint Queued Standard """.split()


#------------------------------------------------------------------------------
# Class SwServiceImplPolicyEnum
#------------------------------------------------------------------------------
class SwServiceImplPolicyEnum(ENUM):
	"""Defines SwServiceImplPolicyEnum Enums"""
	_names_ = """undefined Inline InlineConditional Macro Standard """.split()


#------------------------------------------------------------------------------
# Class DisplayPresentationEnum
#------------------------------------------------------------------------------
class DisplayPresentationEnum(ENUM):
	"""Defines DisplayPresentationEnum Enums"""
	_names_ = """undefined PresentationContinuous PresentationDiscrete """.split()


#------------------------------------------------------------------------------
# Class TDEventBswInternalBehaviorTypeEnum
#------------------------------------------------------------------------------
class TDEventBswInternalBehaviorTypeEnum(ENUM):
	"""Defines TDEventBswInternalBehaviorTypeEnum Enums"""
	_names_ = """undefined BswModuleEntityActivated BswModuleEntityStarted BswModuleEntityTerminated """.split()


#------------------------------------------------------------------------------
# Class TDEventBswModeDeclarationTypeEnum
#------------------------------------------------------------------------------
class TDEventBswModeDeclarationTypeEnum(ENUM):
	"""Defines TDEventBswModeDeclarationTypeEnum Enums"""
	_names_ = """undefined ModeDeclarationRequested ModeDeclarationSwitchCompleted ModeDeclarationSwitchInitiated """.split()


#------------------------------------------------------------------------------
# Class TDEventBswModuleTypeEnum
#------------------------------------------------------------------------------
class TDEventBswModuleTypeEnum(ENUM):
	"""Defines TDEventBswModuleTypeEnum Enums"""
	_names_ = """undefined BswMEntryCallReturned BswMEntryCalled """.split()


#------------------------------------------------------------------------------
# Class TDEventFrameTypeEnum
#------------------------------------------------------------------------------
class TDEventFrameTypeEnum(ENUM):
	"""Defines TDEventFrameTypeEnum Enums"""
	_names_ = """undefined FrameQueuedForTransmission FrameReceivedByIf FrameTransmittedOnBus """.split()


#------------------------------------------------------------------------------
# Class TDEventIPduTypeEnum
#------------------------------------------------------------------------------
class TDEventIPduTypeEnum(ENUM):
	"""Defines TDEventIPduTypeEnum Enums"""
	_names_ = """undefined IPduReceivedByCom IPduSentToIf """.split()


#------------------------------------------------------------------------------
# Class TDEventISignalTypeEnum
#------------------------------------------------------------------------------
class TDEventISignalTypeEnum(ENUM):
	"""Defines TDEventISignalTypeEnum Enums"""
	_names_ = """undefined ISignalAvailableForRte ISignalSentToCom """.split()


#------------------------------------------------------------------------------
# Class TDEventModeDeclarationTypeEnum
#------------------------------------------------------------------------------
class TDEventModeDeclarationTypeEnum(ENUM):
	"""Defines TDEventModeDeclarationTypeEnum Enums"""
	_names_ = """undefined ModeDeclarationSwitchCompleted ModeDeclarationSwitchInitiated """.split()


#------------------------------------------------------------------------------
# Class TDEventOperationTypeEnum
#------------------------------------------------------------------------------
class TDEventOperationTypeEnum(ENUM):
	"""Defines TDEventOperationTypeEnum Enums"""
	_names_ = """undefined OperationCallReceived OperationCallResponseReceived OperationCallResponseSent OperationCalled """.split()


#------------------------------------------------------------------------------
# Class TDEventSwcInternalBehaviorTypeEnum
#------------------------------------------------------------------------------
class TDEventSwcInternalBehaviorTypeEnum(ENUM):
	"""Defines TDEventSwcInternalBehaviorTypeEnum Enums"""
	_names_ = """undefined RunnableEntityActivated RunnableEntityStarted RunnableEntityTerminated RunnableEntityVariableAccess """.split()


#------------------------------------------------------------------------------
# Class TDEventTriggerTypeEnum
#------------------------------------------------------------------------------
class TDEventTriggerTypeEnum(ENUM):
	"""Defines TDEventTriggerTypeEnum Enums"""
	_names_ = """undefined TriggerActivated TriggerReleased """.split()


#------------------------------------------------------------------------------
# Class TDEventVariableDataPrototypeTypeEnum
#------------------------------------------------------------------------------
class TDEventVariableDataPrototypeTypeEnum(ENUM):
	"""Defines TDEventVariableDataPrototypeTypeEnum Enums"""
	_names_ = """undefined VariableDataPrototypeReceived VariableDataPrototypeSent """.split()


#------------------------------------------------------------------------------
# Class TDEventFrameEthernetTypeEnum
#------------------------------------------------------------------------------
class TDEventFrameEthernetTypeEnum(ENUM):
	"""Defines TDEventFrameEthernetTypeEnum Enums"""
	_names_ = """undefined FrameEthernetQueuedForTransmission FrameEthernetReceivedByIf FrameEthernetReceivedOnBus FrameEthernetSentOnBus """.split()


#------------------------------------------------------------------------------
# Class EventOccurrenceKindEnum
#------------------------------------------------------------------------------
class EventOccurrenceKindEnum(ENUM):
	"""Defines EventOccurrenceKindEnum Enums"""
	_names_ = """undefined MultipleOccurrences SingleOccurrence """.split()


#------------------------------------------------------------------------------
# Class ExecutionOrderConstraintTypeEnum
#------------------------------------------------------------------------------
class ExecutionOrderConstraintTypeEnum(ENUM):
	"""Defines ExecutionOrderConstraintTypeEnum Enums"""
	_names_ = """undefined HierarchicalEoc OrdinaryEoc RepetitiveEoc """.split()


#------------------------------------------------------------------------------
# Class ExecutionTimeTypeEnum
#------------------------------------------------------------------------------
class ExecutionTimeTypeEnum(ENUM):
	"""Defines ExecutionTimeTypeEnum Enums"""
	_names_ = """undefined Gross Net """.split()


#------------------------------------------------------------------------------
# Class LatencyConstraintTypeEnum
#------------------------------------------------------------------------------
class LatencyConstraintTypeEnum(ENUM):
	"""Defines LatencyConstraintTypeEnum Enums"""
	_names_ = """undefined Age Reaction """.split()


#------------------------------------------------------------------------------
# Class SynchronizationTypeEnum
#------------------------------------------------------------------------------
class SynchronizationTypeEnum(ENUM):
	"""Defines SynchronizationTypeEnum Enums"""
	_names_ = """undefined ResponseSynchronization StimulusSynchronization """.split()


#------------------------------------------------------------------------------
# Class TDEventServiceInstanceDiscoveryTypeEnum
#------------------------------------------------------------------------------
class TDEventServiceInstanceDiscoveryTypeEnum(ENUM):
	"""Defines TDEventServiceInstanceDiscoveryTypeEnum Enums"""
	_names_ = """undefined AdaptiveServiceFindCompleted AdaptiveServiceFindStarted AdaptiveServiceOfferCompleted AdaptiveServiceOfferStarted AdaptiveServiceStopSubscriptionCompleted AdaptiveServiceStopSubscriptionStarted AdaptiveServiceSubscriptionAcknowledgeCompleted AdaptiveServiceSubscriptionAcknowledgeStarted AdaptiveServiceSubscriptionCompleted AdaptiveServiceSubscriptionStarted """.split()


#------------------------------------------------------------------------------
# Class TDEventServiceInstanceEventTypeEnum
#------------------------------------------------------------------------------
class TDEventServiceInstanceEventTypeEnum(ENUM):
	"""Defines TDEventServiceInstanceEventTypeEnum Enums"""
	_names_ = """undefined AdaptiveEventReceived AdaptiveEventSent """.split()


#------------------------------------------------------------------------------
# Class TDEventServiceInstanceFieldTypeEnum
#------------------------------------------------------------------------------
class TDEventServiceInstanceFieldTypeEnum(ENUM):
	"""Defines TDEventServiceInstanceFieldTypeEnum Enums"""
	_names_ = """undefined AdaptiveFieldGetterCalled AdaptiveFieldGetterCompleted AdaptiveFieldNotificationReceived AdaptiveFieldNotificationSent AdaptiveFieldSetterCalled AdaptiveFieldSetterCompleted """.split()


#------------------------------------------------------------------------------
# Class TDEventServiceInstanceMethodTypeEnum
#------------------------------------------------------------------------------
class TDEventServiceInstanceMethodTypeEnum(ENUM):
	"""Defines TDEventServiceInstanceMethodTypeEnum Enums"""
	_names_ = """undefined AdaptiveMethodCallReceived AdaptiveMethodCalled AdaptiveMethodResponseReceived AdaptiveMethodResponseSent """.split()


#------------------------------------------------------------------------------
# Class SignalServiceTranslationControlEnum
#------------------------------------------------------------------------------
class SignalServiceTranslationControlEnum(ENUM):
	"""Defines SignalServiceTranslationControlEnum Enums"""
	_names_ = """undefined AllPartialNetworksActive AnyPartialNetworkActive PartialNetwork ServiceDiscovery TranslationStart """.split()


#------------------------------------------------------------------------------
# Class DiagnosticAudienceEnum
#------------------------------------------------------------------------------
class DiagnosticAudienceEnum(ENUM):
	"""Defines DiagnosticAudienceEnum Enums"""
	_names_ = """undefined AfterSales Aftermarket Development Manufacturing Supplier """.split()


#------------------------------------------------------------------------------
# Class DiagnosticClearDtcNotificationEnum
#------------------------------------------------------------------------------
class DiagnosticClearDtcNotificationEnum(ENUM):
	"""Defines DiagnosticClearDtcNotificationEnum Enums"""
	_names_ = """undefined Finish Start """.split()


#------------------------------------------------------------------------------
# Class DiagnosticDenominatorConditionEnum
#------------------------------------------------------------------------------
class DiagnosticDenominatorConditionEnum(ENUM):
	"""Defines DiagnosticDenominatorConditionEnum Enums"""
	_names_ = """undefined _500Miles Coldstart Csers Evap Individual Obd """.split()


#------------------------------------------------------------------------------
# Class DiagnosticProcessingStyleEnum
#------------------------------------------------------------------------------
class DiagnosticProcessingStyleEnum(ENUM):
	"""Defines DiagnosticProcessingStyleEnum Enums"""
	_names_ = """undefined ProcessingStyleAsynchronous ProcessingStyleAsynchronousWithError ProcessingStyleSynchronous """.split()


#------------------------------------------------------------------------------
# Class DiagnosticRoutineTypeEnum
#------------------------------------------------------------------------------
class DiagnosticRoutineTypeEnum(ENUM):
	"""Defines DiagnosticRoutineTypeEnum Enums"""
	_names_ = """undefined Asynchronous Synchronous """.split()


#------------------------------------------------------------------------------
# Class DiagnosticServiceRequestCallbackTypeEnum
#------------------------------------------------------------------------------
class DiagnosticServiceRequestCallbackTypeEnum(ENUM):
	"""Defines DiagnosticServiceRequestCallbackTypeEnum Enums"""
	_names_ = """undefined RequestCallbackTypeManufacturer RequestCallbackTypeSupplier """.split()


#------------------------------------------------------------------------------
# Class DiagnosticValueAccessEnum
#------------------------------------------------------------------------------
class DiagnosticValueAccessEnum(ENUM):
	"""Defines DiagnosticValueAccessEnum Enums"""
	_names_ = """undefined ReadOnly ReadWrite WriteOnly """.split()


#------------------------------------------------------------------------------
# Class EventAcceptanceStatusEnum
#------------------------------------------------------------------------------
class EventAcceptanceStatusEnum(ENUM):
	"""Defines EventAcceptanceStatusEnum Enums"""
	_names_ = """undefined EventAcceptanceDisabled EventAcceptanceEnabled """.split()


#------------------------------------------------------------------------------
# Class MaxCommModeEnum
#------------------------------------------------------------------------------
class MaxCommModeEnum(ENUM):
	"""Defines MaxCommModeEnum Enums"""
	_names_ = """undefined Full NONE Silent """.split()


#------------------------------------------------------------------------------
# Class NvBlockNeedsReliabilityEnum
#------------------------------------------------------------------------------
class NvBlockNeedsReliabilityEnum(ENUM):
	"""Defines NvBlockNeedsReliabilityEnum Enums"""
	_names_ = """undefined ErrorCorrection ErrorDetection NoProtection """.split()


#------------------------------------------------------------------------------
# Class NvBlockNeedsWritingPriorityEnum
#------------------------------------------------------------------------------
class NvBlockNeedsWritingPriorityEnum(ENUM):
	"""Defines NvBlockNeedsWritingPriorityEnum Enums"""
	_names_ = """undefined High Low Medium """.split()


#------------------------------------------------------------------------------
# Class ObdRatioConnectionKindEnum
#------------------------------------------------------------------------------
class ObdRatioConnectionKindEnum(ENUM):
	"""Defines ObdRatioConnectionKindEnum Enums"""
	_names_ = """undefined ApiUse Observer """.split()


#------------------------------------------------------------------------------
# Class OperationCycleTypeEnum
#------------------------------------------------------------------------------
class OperationCycleTypeEnum(ENUM):
	"""Defines OperationCycleTypeEnum Enums"""
	_names_ = """undefined Ignition ObdDcy Other Power Time Warmup """.split()


#------------------------------------------------------------------------------
# Class ServiceDiagnosticRelevanceEnum
#------------------------------------------------------------------------------
class ServiceDiagnosticRelevanceEnum(ENUM):
	"""Defines ServiceDiagnosticRelevanceEnum Enums"""
	_names_ = """undefined IsNotRelevant IsRelevant """.split()


#------------------------------------------------------------------------------
# Class ServiceProviderEnum
#------------------------------------------------------------------------------
class ServiceProviderEnum(ENUM):
	"""Defines ServiceProviderEnum Enums"""
	_names_ = """undefined AnyStandardized BasicSoftwareModeManager ComManager CryptoKeyManagement CryptoServiceManager DefaultErrorTracer DiagnosticCommunicationManager DiagnosticEventManager DiagnosticLogAndTrace EcuManager ErrorTracer FunctionInhibitionManager HardwareTestManager IntrusionDetectionSecurityManagement J1939Dcm J1939RequestManager NonVolatileRamManager OperatingSystem SecureOnBoardCommunication SyncBaseTimeManager V2XFacilities V2XManagement VendorSpecific WatchDogManager """.split()


#------------------------------------------------------------------------------
# Class StorageConditionStatusEnum
#------------------------------------------------------------------------------
class StorageConditionStatusEnum(ENUM):
	"""Defines StorageConditionStatusEnum Enums"""
	_names_ = """undefined EventStorageDisabled EventStorageEnabled """.split()


#------------------------------------------------------------------------------
# Class VerificationStatusIndicationModeEnum
#------------------------------------------------------------------------------
class VerificationStatusIndicationModeEnum(ENUM):
	"""Defines VerificationStatusIndicationModeEnum Enums"""
	_names_ = """undefined FailureAndSuccess FailureOnly """.split()


#------------------------------------------------------------------------------
# Class ModeActivationKindEnum
#------------------------------------------------------------------------------
class ModeActivationKindEnum(ENUM):
	"""Defines ModeActivationKindEnum Enums"""
	_names_ = """undefined OnEntry OnExit OnTransition """.split()


#------------------------------------------------------------------------------
# Class ModeErrorReactionPolicyEnum
#------------------------------------------------------------------------------
class ModeErrorReactionPolicyEnum(ENUM):
	"""Defines ModeErrorReactionPolicyEnum Enums"""
	_names_ = """undefined DefaultMode LastMode """.split()


#------------------------------------------------------------------------------
# Class RptAccessEnum
#------------------------------------------------------------------------------
class RptAccessEnum(ENUM):
	"""Defines RptAccessEnum Enums"""
	_names_ = """undefined Enabled NONE Protected """.split()


#------------------------------------------------------------------------------
# Class RptEnablerImplTypeEnum
#------------------------------------------------------------------------------
class RptEnablerImplTypeEnum(ENUM):
	"""Defines RptEnablerImplTypeEnum Enums"""
	_names_ = """undefined NONE RptEnablerRam RptEnablerRamAndRom RptEnablerRom """.split()


#------------------------------------------------------------------------------
# Class RptExecutionControlEnum
#------------------------------------------------------------------------------
class RptExecutionControlEnum(ENUM):
	"""Defines RptExecutionControlEnum Enums"""
	_names_ = """undefined Conditional NONE """.split()


#------------------------------------------------------------------------------
# Class RptPreparationEnum
#------------------------------------------------------------------------------
class RptPreparationEnum(ENUM):
	"""Defines RptPreparationEnum Enums"""
	_names_ = """undefined NONE RptLevel1 RptLevel2 RptLevel3 """.split()


#------------------------------------------------------------------------------
# Class ApiPrincipleEnum
#------------------------------------------------------------------------------
class ApiPrincipleEnum(ENUM):
	"""Defines ApiPrincipleEnum Enums"""
	_names_ = """undefined Common PerExecutable """.split()


#------------------------------------------------------------------------------
# Class ReentrancyLevelEnum
#------------------------------------------------------------------------------
class ReentrancyLevelEnum(ENUM):
	"""Defines ReentrancyLevelEnum Enums"""
	_names_ = """undefined MulticoreReentrant NonReentrant SingleCoreReentrant """.split()


#------------------------------------------------------------------------------
# Class DependencyUsageEnum
#------------------------------------------------------------------------------
class DependencyUsageEnum(ENUM):
	"""Defines DependencyUsageEnum Enums"""
	_names_ = """undefined Build Codegeneration Compile Execute Link """.split()


#------------------------------------------------------------------------------
# Class ProgramminglanguageEnum
#------------------------------------------------------------------------------
class ProgramminglanguageEnum(ENUM):
	"""Defines ProgramminglanguageEnum Enums"""
	_names_ = """undefined C Cpp Java """.split()


#------------------------------------------------------------------------------
# Class ArrayImplPolicyEnum
#------------------------------------------------------------------------------
class ArrayImplPolicyEnum(ENUM):
	"""Defines ArrayImplPolicyEnum Enums"""
	_names_ = """undefined PayloadAsArray PayloadAsPointerToArray """.split()


#------------------------------------------------------------------------------
# Class ArraySizeSemanticsEnum
#------------------------------------------------------------------------------
class ArraySizeSemanticsEnum(ENUM):
	"""Defines ArraySizeSemanticsEnum Enums"""
	_names_ = """undefined FixedSize VariableSize """.split()


#------------------------------------------------------------------------------
# Class DataFilterTypeEnum
#------------------------------------------------------------------------------
class DataFilterTypeEnum(ENUM):
	"""Defines DataFilterTypeEnum Enums"""
	_names_ = """undefined Always MaskedNewDiffersMaskedOld MaskedNewDiffersX MaskedNewEqualsX Never NewIsOutside NewIsWithin OneEveryN """.split()


#------------------------------------------------------------------------------
# Class BswCallTypeEnum
#------------------------------------------------------------------------------
class BswCallTypeEnum(ENUM):
	"""Defines BswCallTypeEnum Enums"""
	_names_ = """undefined Callback Callout Interrupt Regular Scheduled """.split()


#------------------------------------------------------------------------------
# Class BswEntryKindEnum
#------------------------------------------------------------------------------
class BswEntryKindEnum(ENUM):
	"""Defines BswEntryKindEnum Enums"""
	_names_ = """undefined Abstract Concrete """.split()


#------------------------------------------------------------------------------
# Class BswEntryRelationshipEnum
#------------------------------------------------------------------------------
class BswEntryRelationshipEnum(ENUM):
	"""Defines BswEntryRelationshipEnum Enums"""
	_names_ = """undefined DerivedFrom """.split()


#------------------------------------------------------------------------------
# Class BswExecutionContextEnum
#------------------------------------------------------------------------------
class BswExecutionContextEnum(ENUM):
	"""Defines BswExecutionContextEnum Enums"""
	_names_ = """undefined Hook InterruptCat1 InterruptCat2 Task Unspecified """.split()


#------------------------------------------------------------------------------
# Class BswInterruptCategoryEnum
#------------------------------------------------------------------------------
class BswInterruptCategoryEnum(ENUM):
	"""Defines BswInterruptCategoryEnum Enums"""
	_names_ = """undefined Cat1 Cat2 """.split()


#------------------------------------------------------------------------------
# Class IntervalTypeEnum
#------------------------------------------------------------------------------
class IntervalTypeEnum(ENUM):
	"""Defines IntervalTypeEnum Enums"""
	_names_ = """undefined Closed Open """.split()


#------------------------------------------------------------------------------
# Class ScaleConstrValidityEnum
#------------------------------------------------------------------------------
class ScaleConstrValidityEnum(ENUM):
	"""Defines ScaleConstrValidityEnum Enums"""
	_names_ = """undefined NotAvailable NotDefined NotValid Valid """.split()


#------------------------------------------------------------------------------
# Class SoftwareClusterDependencyLogicalOperatorEnum
#------------------------------------------------------------------------------
class SoftwareClusterDependencyLogicalOperatorEnum(ENUM):
	"""Defines SoftwareClusterDependencyLogicalOperatorEnum Enums"""
	_names_ = """undefined LogicalAnd LogicalOr """.split()


#------------------------------------------------------------------------------
# Class SoftwareClusterDependencyOperatorEnum
#------------------------------------------------------------------------------
class SoftwareClusterDependencyOperatorEnum(ENUM):
	"""Defines SoftwareClusterDependencyOperatorEnum Enums"""
	_names_ = """undefined IsEqual IsGreaterThan IsGreaterThanOrEqual IsLessThan IsLessThanOrEqual """.split()


#------------------------------------------------------------------------------
# Class SoftwarePackageActionTypeEnum
#------------------------------------------------------------------------------
class SoftwarePackageActionTypeEnum(ENUM):
	"""Defines SoftwarePackageActionTypeEnum Enums"""
	_names_ = """undefined Install Remove Update """.split()


#------------------------------------------------------------------------------
# Class SoftwarePackageActivationActionEnum
#------------------------------------------------------------------------------
class SoftwarePackageActivationActionEnum(ENUM):
	"""Defines SoftwarePackageActivationActionEnum Enums"""
	_names_ = """undefined Nothing Reboot RestartApplication """.split()


#------------------------------------------------------------------------------
# Class SoftwarePackageStoringEnum
#------------------------------------------------------------------------------
class SoftwarePackageStoringEnum(ENUM):
	"""Defines SoftwarePackageStoringEnum Enums"""
	_names_ = """undefined NONE Ucm UcmMaster """.split()


#------------------------------------------------------------------------------
# Class VehicleDriverNotificationEnum
#------------------------------------------------------------------------------
class VehicleDriverNotificationEnum(ENUM):
	"""Defines VehicleDriverNotificationEnum Enums"""
	_names_ = """undefined Activate Cancel Finish Process RollBack Transfer """.split()


#------------------------------------------------------------------------------
# Class SoftwareClusterInstallationBehaviorEnum
#------------------------------------------------------------------------------
class SoftwareClusterInstallationBehaviorEnum(ENUM):
	"""Defines SoftwareClusterInstallationBehaviorEnum Enums"""
	_names_ = """undefined CanBeRemoved CannotBeRemoved """.split()


#------------------------------------------------------------------------------
# Class SoftwareClusterDiagnosticAddressSemanticsEnum
#------------------------------------------------------------------------------
class SoftwareClusterDiagnosticAddressSemanticsEnum(ENUM):
	"""Defines SoftwareClusterDiagnosticAddressSemanticsEnum Enums"""
	_names_ = """undefined FunctionalAddress PhysicalAddress """.split()


#------------------------------------------------------------------------------
# Class SerializationTechnologyEnum
#------------------------------------------------------------------------------
class SerializationTechnologyEnum(ENUM):
	"""Defines SerializationTechnologyEnum Enums"""
	_names_ = """undefined SignalBased Someip """.split()


#------------------------------------------------------------------------------
# Class AccessControlEnum
#------------------------------------------------------------------------------
class AccessControlEnum(ENUM):
	"""Defines AccessControlEnum Enums"""
	_names_ = """undefined Custom Modeled """.split()


#------------------------------------------------------------------------------
# Class DdsServiceInstanceDiscoveryTypeEnum
#------------------------------------------------------------------------------
class DdsServiceInstanceDiscoveryTypeEnum(ENUM):
	"""Defines DdsServiceInstanceDiscoveryTypeEnum Enums"""
	_names_ = """undefined DomainParticipantUserDataQos Topic """.split()


#------------------------------------------------------------------------------
# Class DdsServiceInstanceResourceIdentifierTypeEnum
#------------------------------------------------------------------------------
class DdsServiceInstanceResourceIdentifierTypeEnum(ENUM):
	"""Defines DdsServiceInstanceResourceIdentifierTypeEnum Enums"""
	_names_ = """undefined InstanceId Partition TopicPrefix """.split()


#------------------------------------------------------------------------------
# Class UdpCollectionTriggerEnum
#------------------------------------------------------------------------------
class UdpCollectionTriggerEnum(ENUM):
	"""Defines UdpCollectionTriggerEnum Enums"""
	_names_ = """undefined Always Never """.split()


#------------------------------------------------------------------------------
# Class DdsProtectionKindEnum
#------------------------------------------------------------------------------
class DdsProtectionKindEnum(ENUM):
	"""Defines DdsProtectionKindEnum Enums"""
	_names_ = """undefined EncryptAndSign EncryptAndSignWithOriginAuthentication NONE Sign SignWithOriginAuthentication """.split()


#------------------------------------------------------------------------------
# Class IPTransportProtocolEnum
#------------------------------------------------------------------------------
class IPTransportProtocolEnum(ENUM):
	"""Defines IPTransportProtocolEnum Enums"""
	_names_ = """undefined Tcp Udp """.split()


#------------------------------------------------------------------------------
# Class StateManagementCompareEnum
#------------------------------------------------------------------------------
class StateManagementCompareEnum(ENUM):
	"""Defines StateManagementCompareEnum Enums"""
	_names_ = """undefined IsEqual """.split()


#------------------------------------------------------------------------------
# Class FunctionalClusterPersistencyAccessEnum
#------------------------------------------------------------------------------
class FunctionalClusterPersistencyAccessEnum(ENUM):
	"""Defines FunctionalClusterPersistencyAccessEnum Enums"""
	_names_ = """undefined Read ReadWrite Write """.split()


#------------------------------------------------------------------------------
# Class PersistencyRedundancyHandlingScopeEnum
#------------------------------------------------------------------------------
class PersistencyRedundancyHandlingScopeEnum(ENUM):
	"""Defines PersistencyRedundancyHandlingScopeEnum Enums"""
	_names_ = """undefined PersistencyRedundancyHandlingScopeElement PersistencyRedundancyHandlingScopeStorage """.split()


#------------------------------------------------------------------------------
# Class FirewallActionEnum
#------------------------------------------------------------------------------
class FirewallActionEnum(ENUM):
	"""Defines FirewallActionEnum Enums"""
	_names_ = """undefined Allow Block """.split()


#------------------------------------------------------------------------------
# Class CryptoKeySlotUsageEnum
#------------------------------------------------------------------------------
class CryptoKeySlotUsageEnum(ENUM):
	"""Defines CryptoKeySlotUsageEnum Enums"""
	_names_ = """undefined Encryption Verification """.split()


#------------------------------------------------------------------------------
# Class DoIpEidRetrievalEnum
#------------------------------------------------------------------------------
class DoIpEidRetrievalEnum(ENUM):
	"""Defines DoIpEidRetrievalEnum Enums"""
	_names_ = """undefined EidUseApi EidUseConfigValue EidUseMac """.split()


#------------------------------------------------------------------------------
# Class NmHandleMappingDirectionEnum
#------------------------------------------------------------------------------
class NmHandleMappingDirectionEnum(ENUM):
	"""Defines NmHandleMappingDirectionEnum Enums"""
	_names_ = """undefined FunctionGroupStateToNmHandle NmHandleActiveToFunctionGroupState NmHandleInactiveToFunctionGroupState """.split()


#------------------------------------------------------------------------------
# Class RequestTypeEnum
#------------------------------------------------------------------------------
class RequestTypeEnum(ENUM):
	"""Defines RequestTypeEnum Enums"""
	_names_ = """undefined Functional Physical """.split()


#------------------------------------------------------------------------------
# Class TrustedPlatformExecutableLaunchBehaviorEnum
#------------------------------------------------------------------------------
class TrustedPlatformExecutableLaunchBehaviorEnum(ENUM):
	"""Defines TrustedPlatformExecutableLaunchBehaviorEnum Enums"""
	_names_ = """undefined MonitorMode NoTrustedPlatformSupport StrictMode """.split()


#------------------------------------------------------------------------------
# Class LogTraceDefaultLogLevelEnum
#------------------------------------------------------------------------------
class LogTraceDefaultLogLevelEnum(ENUM):
	"""Defines LogTraceDefaultLogLevelEnum Enums"""
	_names_ = """undefined Debug Error Fatal Info Off Verbose Warn """.split()


#------------------------------------------------------------------------------
# Class TerminationBehaviorEnum
#------------------------------------------------------------------------------
class TerminationBehaviorEnum(ENUM):
	"""Defines TerminationBehaviorEnum Enums"""
	_names_ = """undefined ProcessIsNotSelfTerminating ProcessIsSelfTerminating """.split()


#------------------------------------------------------------------------------
# Class TransportLayerProtocolEnum
#------------------------------------------------------------------------------
class TransportLayerProtocolEnum(ENUM):
	"""Defines TransportLayerProtocolEnum Enums"""
	_names_ = """undefined Tcp Udp """.split()


#------------------------------------------------------------------------------
# Class SecOcJobSemanticEnum
#------------------------------------------------------------------------------
class SecOcJobSemanticEnum(ENUM):
	"""Defines SecOcJobSemanticEnum Enums"""
	_names_ = """undefined Authenticate Verify """.split()


#------------------------------------------------------------------------------
# Class BuildTypeEnum
#------------------------------------------------------------------------------
class BuildTypeEnum(ENUM):
	"""Defines BuildTypeEnum Enums"""
	_names_ = """undefined BuildTypeDebug BuildTypeRelease """.split()


#------------------------------------------------------------------------------
# Class SearchIntentionEnum
#------------------------------------------------------------------------------
class SearchIntentionEnum(ENUM):
	"""Defines SearchIntentionEnum Enums"""
	_names_ = """undefined SearchForAllInstances SearchForSpecificInstance """.split()


#------------------------------------------------------------------------------
# Class PersistencyCollectionLevelUpdateStrategyEnum
#------------------------------------------------------------------------------
class PersistencyCollectionLevelUpdateStrategyEnum(ENUM):
	"""Defines PersistencyCollectionLevelUpdateStrategyEnum Enums"""
	_names_ = """undefined Delete KeepExisting """.split()


#------------------------------------------------------------------------------
# Class PersistencyElementLevelUpdateStrategyEnum
#------------------------------------------------------------------------------
class PersistencyElementLevelUpdateStrategyEnum(ENUM):
	"""Defines PersistencyElementLevelUpdateStrategyEnum Enums"""
	_names_ = """undefined Delete KeepExisting Overwrite """.split()


#------------------------------------------------------------------------------
# Class TimeSynchronizationKindEnum
#------------------------------------------------------------------------------
class TimeSynchronizationKindEnum(ENUM):
	"""Defines TimeSynchronizationKindEnum Enums"""
	_names_ = """undefined Offset Synchronized """.split()


#------------------------------------------------------------------------------
# Class FieldAccessEnum
#------------------------------------------------------------------------------
class FieldAccessEnum(ENUM):
	"""Defines FieldAccessEnum Enums"""
	_names_ = """undefined Getter GetterSetter Setter """.split()


#------------------------------------------------------------------------------
# Class CryptoKeySlotTypeEnum
#------------------------------------------------------------------------------
class CryptoKeySlotTypeEnum(ENUM):
	"""Defines CryptoKeySlotTypeEnum Enums"""
	_names_ = """undefined Application Machine """.split()


#------------------------------------------------------------------------------
# Class CryptoObjectTypeEnum
#------------------------------------------------------------------------------
class CryptoObjectTypeEnum(ENUM):
	"""Defines CryptoObjectTypeEnum Enums"""
	_names_ = """undefined PrivateKey PublicKey SecretSeed Signature SymmetricKey Undefined_ """.split()


#------------------------------------------------------------------------------
# Class ClientIntentEnum
#------------------------------------------------------------------------------
class ClientIntentEnum(ENUM):
	"""Defines ClientIntentEnum Enums"""
	_names_ = """undefined WillCall WontCall """.split()


#------------------------------------------------------------------------------
# Class PersistencyRedundancyEnum
#------------------------------------------------------------------------------
class PersistencyRedundancyEnum(ENUM):
	"""Defines PersistencyRedundancyEnum Enums"""
	_names_ = """undefined NONE Redundant RedundantPerElement """.split()


#------------------------------------------------------------------------------
# Class ReceiverIntentEnum
#------------------------------------------------------------------------------
class ReceiverIntentEnum(ENUM):
	"""Defines ReceiverIntentEnum Enums"""
	_names_ = """undefined WillReceive WontReceive """.split()


#------------------------------------------------------------------------------
# Class SenderIntentEnum
#------------------------------------------------------------------------------
class SenderIntentEnum(ENUM):
	"""Defines SenderIntentEnum Enums"""
	_names_ = """undefined WillSend WontSend """.split()


#------------------------------------------------------------------------------
# Class ExecutionStateReportingBehaviorEnum
#------------------------------------------------------------------------------
class ExecutionStateReportingBehaviorEnum(ENUM):
	"""Defines ExecutionStateReportingBehaviorEnum Enums"""
	_names_ = """undefined DoesNotReportExecutionState ReportsExecutionState """.split()


