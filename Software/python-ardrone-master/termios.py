# Generated by h2py from /usr/include/termios.h

# Included from sys/termios.h

# Included from sys/feature_tests.h
_POSIX_C_SOURCE = 1

# Included from sys/ttydev.h
B0 = 0
B50 = 1
B75 = 2
B110 = 3
B134 = 4
B150 = 5
B200 = 6
B300 = 7
B600 = 8
B1200 = 9
B1800 = 10
B2400 = 11
B4800 = 12
B9600 = 13
B19200 = 14
B38400 = 15
EXTA = 14
EXTB = 15

# Included from sys/types.h

# Included from sys/machtypes.h

# Included from sys/isa_defs.h
SHRT_MIN = -32768
SHRT_MAX = 32767
INT_MIN = (-2147483647-1)
INT_MAX = 2147483647
LONG_MIN = (-2147483647-1)
LONG_MAX = 2147483647
P_MYID = (-1)

# Included from sys/select.h

# Included from sys/time.h
DST_NONE = 0
DST_USA = 1
DST_AUST = 2
DST_WET = 3
DST_MET = 4
DST_EET = 5
DST_CAN = 6
DST_GB = 7
DST_RUM = 8
DST_TUR = 9
DST_AUSTALT = 10
ITIMER_REAL = 0
ITIMER_VIRTUAL = 1
ITIMER_PROF = 2
ITIMER_REALPROF = 3
SEC = 1
MILLISEC = 1000
MICROSEC = 1000000
NANOSEC = 1000000000
CLOCK_REALTIME = 0
CLOCK_VIRTUAL = 1
CLOCK_PROF = 2
TIMER_RELTIME = 0x0
TIMER_ABSTIME = 0x1

# Included from sys/mutex.h

# Included from sys/dki_lkinfo.h

# Included from sys/dl.h
NOSTATS = 1
LSB_NLKDS = 91
def MUTEX_HELD(x): return (mutex_owned(x))


# Included from time.h
NULL = 0
CLOCKS_PER_SEC = 1000000

# Included from sys/siginfo.h
SIGEV_NONE = 1
SIGEV_SIGNAL = 2
SI_NOINFO = 32767
SI_USER = 0
SI_LWP = (-1)
SI_QUEUE = (-2)
SI_TIMER = (-3)
SI_ASYNCIO = (-4)
SI_MESGQ = (-5)

# Included from sys/machsig.h
ILL_ILLOPC = 1
ILL_ILLOPN = 2
ILL_ILLADR = 3
ILL_ILLTRP = 4
ILL_PRVOPC = 5
ILL_PRVREG = 6
ILL_COPROC = 7
ILL_BADSTK = 8
NSIGILL = 8
EMT_TAGOVF = 1
NSIGEMT = 1
FPE_INTDIV = 1
FPE_INTOVF = 2
FPE_FLTDIV = 3
FPE_FLTOVF = 4
FPE_FLTUND = 5
FPE_FLTRES = 6
FPE_FLTINV = 7
FPE_FLTSUB = 8
NSIGFPE = 8
SEGV_MAPERR = 1
SEGV_ACCERR = 2
NSIGSEGV = 2
BUS_ADRALN = 1
BUS_ADRERR = 2
BUS_OBJERR = 3
NSIGBUS = 3
TRAP_BRKPT = 1
TRAP_TRACE = 2
NSIGTRAP = 2
CLD_EXITED = 1
CLD_KILLED = 2
CLD_DUMPED = 3
CLD_TRAPPED = 4
CLD_STOPPED = 5
CLD_CONTINUED = 6
NSIGCLD = 6
POLL_IN = 1
POLL_OUT = 2
POLL_MSG = 3
POLL_ERR = 4
POLL_PRI = 5
POLL_HUP = 6
NSIGPOLL = 6
PROF_SIG = 1
NSIGPROF = 1
SI_MAXSZ = 128
FD_SETSIZE = 1024
NBBY = 8
_POSIX_VDISABLE = 0
def CTRL(c): return ((c)&037)

IBSHIFT = 16
NCC = 8
NCCS = 19
VINTR = 0
VQUIT = 1
VERASE = 2
VKILL = 3
VEOF = 4
VEOL = 5
VEOL2 = 6
VMIN = 4
VTIME = 5
VSWTCH = 7
VSTART = 8
VSTOP = 9
VSUSP = 10
VDSUSP = 11
VREPRINT = 12
VDISCARD = 13
VWERASE = 14
VLNEXT = 15
VCEOF = NCC
VCEOL = (NCC + 1)
CNUL = 0
CDEL = 0177
CESC = ord('\\')
CINTR = CTRL(ord('c'))
CQUIT = 034
CERASE = 0177
CKILL = CTRL(ord('u'))
CEOT = 04
CEOL = 0
CEOL2 = 0
CEOF = 04
CSTART = 021
CSTOP = 023
CSWTCH = 032
CNSWTCH = 0
CSUSP = CTRL(ord('z'))
CDSUSP = CTRL(ord('y'))
CRPRNT = CTRL(ord('r'))
CFLUSH = CTRL(ord('o'))
CWERASE = CTRL(ord('w'))
CLNEXT = CTRL(ord('v'))
IGNBRK = 0000001
BRKINT = 0000002
IGNPAR = 0000004
PARMRK = 0000010
INPCK = 0000020
ISTRIP = 0000040
INLCR = 0000100
IGNCR = 0000200
ICRNL = 0000400
IUCLC = 0001000
IXON = 0002000
IXANY = 0004000
IXOFF = 0010000
IMAXBEL = 0020000
DOSMODE = 0100000
OPOST = 0000001
OLCUC = 0000002
ONLCR = 0000004
OCRNL = 0000010
ONOCR = 0000020
ONLRET = 0000040
OFILL = 0000100
OFDEL = 0000200
NLDLY = 0000400
NL0 = 0
NL1 = 0000400
CRDLY = 0003000
CR0 = 0
CR1 = 0001000
CR2 = 0002000
CR3 = 0003000
TABDLY = 0014000
TAB0 = 0
TAB1 = 0004000
TAB2 = 0010000
TAB3 = 0014000
XTABS = 0014000
BSDLY = 0020000
BS0 = 0
BS1 = 0020000
VTDLY = 0040000
VT0 = 0
VT1 = 0040000
FFDLY = 0100000
FF0 = 0
FF1 = 0100000
PAGEOUT = 0200000
WRAP = 0400000
CBAUD = 0000017
CSIZE = 0000060
CS5 = 0
CS6 = 0000020
CS7 = 0000040
CS8 = 0000060
CSTOPB = 0000100
CREAD = 0000200
PARENB = 0000400
PARODD = 0001000
HUPCL = 0002000
CLOCAL = 0004000
RCV1EN = 0010000
XMT1EN = 0020000
LOBLK = 0040000
XCLUDE = 0100000
CRTSCTS = 020000000000
CIBAUD = 03600000
PAREXT = 04000000
ISIG = 0000001
ICANON = 0000002
XCASE = 0000004
ECHO = 0000010
ECHOE = 0000020
ECHOK = 0000040
ECHONL = 0000100
NOFLSH = 0000200
TOSTOP = 0000400
ECHOCTL = 0001000
ECHOPRT = 0002000
ECHOKE = 0004000
DEFECHO = 0010000
FLUSHO = 0020000
PENDIN = 0040000
IEXTEN = 0100000
_TIOC = (ord('T')<<8)
TIOC = _TIOC
TCGETA = (_TIOC|1)
TCSETA = (_TIOC|2)
TCSETAW = (_TIOC|3)
TCSETAF = (_TIOC|4)
TCSBRK = (_TIOC|5)
TCXONC = (_TIOC|6)
TCFLSH = (_TIOC|7)
TIOCKBON = (_TIOC|8)
TIOCKBOF = (_TIOC|9)
KBENABLED = (_TIOC|10)
IOCTYPE = 0xff00
TCDSET = (_TIOC|32)
RTS_TOG = (_TIOC|33)
TIOCGWINSZ = (_TIOC|104)
TIOCSWINSZ = (_TIOC|103)
TIOCGSOFTCAR = (_TIOC|105)
TIOCSSOFTCAR = (_TIOC|106)
TCGETS = (_TIOC|13)
TCSETS = (_TIOC|14)
TCSANOW = (_TIOC|14)
TCSETSW = (_TIOC|15)
TCSADRAIN = (_TIOC|15)
TCSETSF = (_TIOC|16)
TCSAFLUSH = (_TIOC|16)
TCIFLUSH = 0
TCOFLUSH = 1
TCIOFLUSH = 2
TCOOFF = 0
TCOON = 1
TCIOFF = 2
TCION = 3
tIOC = (ord('t')<<8)
TIOCGETD = (tIOC|0)
TIOCSETD = (tIOC|1)
TIOCHPCL = (tIOC|2)
TIOCGETP = (tIOC|8)
TIOCSETP = (tIOC|9)
TIOCSETN = (tIOC|10)
TIOCEXCL = (tIOC|13)
TIOCNXCL = (tIOC|14)
TIOCFLUSH = (tIOC|16)
TIOCSETC = (tIOC|17)
TIOCGETC = (tIOC|18)
TIOCLBIS = (tIOC|127)
TIOCLBIC = (tIOC|126)
TIOCLSET = (tIOC|125)
TIOCLGET = (tIOC|124)
TIOCSBRK = (tIOC|123)
TIOCCBRK = (tIOC|122)
TIOCSDTR = (tIOC|121)
TIOCCDTR = (tIOC|120)
TIOCSLTC = (tIOC|117)
TIOCGLTC = (tIOC|116)
TIOCOUTQ = (tIOC|115)
TIOCNOTTY = (tIOC|113)
TIOCSTOP = (tIOC|111)
TIOCSTART = (tIOC|110)
TIOCGPGRP = (tIOC|20)
TIOCSPGRP = (tIOC|21)
TIOCGSID = (tIOC|22)
TIOCSSID = (tIOC|24)
TIOCSTI = (tIOC|23)
TIOCMSET = (tIOC|26)
TIOCMBIS = (tIOC|27)
TIOCMBIC = (tIOC|28)
TIOCMGET = (tIOC|29)
TIOCM_LE = 0001
TIOCM_DTR = 0002
TIOCM_RTS = 0004
TIOCM_ST = 0010
TIOCM_SR = 0020
TIOCM_CTS = 0040
TIOCM_CAR = 0100
TIOCM_CD = TIOCM_CAR
TIOCM_RNG = 0200
TIOCM_RI = TIOCM_RNG
TIOCM_DSR = 0400
TIOCREMOTE = (tIOC|30)
TIOCSIGNAL = (tIOC|31)
LDIOC = (ord('D')<<8)
LDOPEN = (LDIOC|0)
LDCLOSE = (LDIOC|1)
LDCHG = (LDIOC|2)
LDGETT = (LDIOC|8)
LDSETT = (LDIOC|9)
LDSMAP = (LDIOC|110)
LDGMAP = (LDIOC|111)
LDNMAP = (LDIOC|112)
LDEMAP = (LDIOC|113)
LDDMAP = (LDIOC|114)
DIOC = (ord('d')<<8)
DIOCGETP = (DIOC|8)
DIOCSETP = (DIOC|9)
FIORDCHK = ((ord('f')<<8)|3)
B0 = 0
B50 = 1
B75 = 2
B110 = 3
B134 = 4
B150 = 5
B200 = 6
B300 = 7
B600 = 8
B1200 = 9
B1800 = 10
B2400 = 11
B4800 = 12
B9600 = 13
B19200 = 14
B38400 = 15
