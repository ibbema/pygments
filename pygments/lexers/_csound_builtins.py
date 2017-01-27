# -*- coding: utf-8 -*-
"""
    pygments.lexers._csound_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

# Opcodes in Csound 6.08.0 at commit a1159a1 from
#   csound --list-opcodes3
# except for
#   cggoto   <https://csound.github.io/docs/manual/cggoto.html>
#   cigoto   <https://csound.github.io/docs/manual/cigoto.html>
#   cingoto  (undocumented)
#   ckgoto   <https://csound.github.io/docs/manual/ckgoto.html>
#   cngoto   <https://csound.github.io/docs/manual/cngoto.html>
#   cnkgoto  (undocumented)
#   endin    <https://csound.github.io/docs/manual/endin.html
#   endop    <https://csound.github.io/docs/manual/endop.html
#   goto     <https://csound.github.io/docs/manual/goto.html>
#   igoto    <https://csound.github.io/docs/manual/igoto.html>
#   instr    <https://csound.github.io/docs/manual/instr.html>
#   kgoto    <https://csound.github.io/docs/manual/kgoto.html>
#   loop_ge  <https://csound.github.io/docs/manual/loop_ge.html>
#   loop_gt  <https://csound.github.io/docs/manual/loop_gt.html>
#   loop_le  <https://csound.github.io/docs/manual/loop_le.html>
#   loop_lt  <https://csound.github.io/docs/manual/loop_lt.html>
#   opcode   <https://csound.github.io/docs/manual/opcode.html>
#   return   <https://csound.github.io/docs/manual/return.html>
#   rireturn <https://csound.github.io/docs/manual/rireturn.html>
#   rigoto   <https://csound.github.io/docs/manual/rigoto.html>
#   tigoto   <https://csound.github.io/docs/manual/tigoto.html>
#   timout   <https://csound.github.io/docs/manual/timout.html>
# which are treated as keywords in csound.py.

OPCODES = set((
    'ATSadd',
    'ATSaddnz',
    'ATSbufread',
    'ATScross',
    'ATSinfo',
    'ATSinterpread',
    'ATSpartialtap',
    'ATSread',
    'ATSreadnz',
    'ATSsinnoi',
    'FLbox',
    'FLbutBank',
    'FLbutton',
    'FLcloseButton',
    'FLcolor',
    'FLcolor2',
    'FLcount',
    'FLexecButton',
    'FLgetsnap',
    'FLgroup',
    'FLgroupEnd',
    'FLgroup_end',
    'FLhide',
    'FLhvsBox',
    'FLhvsBoxSetValue',
    'FLjoy',
    'FLkeyIn',
    'FLknob',
    'FLlabel',
    'FLloadsnap',
    'FLmouse',
    'FLpack',
    'FLpackEnd',
    'FLpack_end',
    'FLpanel',
    'FLpanelEnd',
    'FLpanel_end',
    'FLprintk',
    'FLprintk2',
    'FLroller',
    'FLrun',
    'FLsavesnap',
    'FLscroll',
    'FLscrollEnd',
    'FLscroll_end',
    'FLsetAlign',
    'FLsetBox',
    'FLsetColor',
    'FLsetColor2',
    'FLsetFont',
    'FLsetPosition',
    'FLsetSize',
    'FLsetSnapGroup',
    'FLsetText',
    'FLsetTextColor',
    'FLsetTextSize',
    'FLsetTextType',
    'FLsetVal',
    'FLsetVal_i',
    'FLsetVali',
    'FLsetsnap',
    'FLshow',
    'FLslidBnk',
    'FLslidBnk2',
    'FLslidBnk2Set',
    'FLslidBnk2Setk',
    'FLslidBnkGetHandle',
    'FLslidBnkSet',
    'FLslidBnkSetk',
    'FLslider',
    'FLtabs',
    'FLtabsEnd',
    'FLtabs_end',
    'FLtext',
    'FLupdate',
    'FLvalue',
    'FLvkeybd',
    'FLvslidBnk',
    'FLvslidBnk2',
    'FLxyin',
    'MixerClear',
    'MixerGetLevel',
    'MixerReceive',
    'MixerSend',
    'MixerSetLevel',
    'MixerSetLevel_i',
    'OSCinit',
    'OSCinitM',
    'OSClisten',
    'OSCsend',
    'S',
    'a',
    'abs',
    'active',
    'adsr',
    'adsyn',
    'adsynt',
    'adsynt2',
    'aftouch',
    'alpass',
    'alwayson',
    'ampdb',
    'ampdbfs',
    'ampmidi',
    'ampmidid',
    'areson',
    'aresonk',
    'atone',
    'atonek',
    'atonex',
    'babo',
    'balance',
    'bamboo',
    'barmodel',
    'bbcutm',
    'bbcuts',
    'betarand',
    'bexprnd',
    'bformdec1',
    'bformenc1',
    'binit',
    'biquad',
    'biquada',
    'birnd',
    'bqrez',
    'buchla',
    'butbp',
    'butbr',
    'buthp',
    'butlp',
    'butterbp',
    'butterbr',
    'butterhp',
    'butterlp',
    'button',
    'buzz',
    'c2r',
    'cabasa',
    'cauchy',
    'cauchyi',
    'ceil',
    'cell',
    'cent',
    'centroid',
    'ceps',
    'cepsinv',
   #'cggoto',
    'chanctrl',
    'changed',
    'changed2',
    'chani',
    'chano',
    'chebyshevpoly',
    'checkbox',
    'chn_S',
    'chn_a',
    'chn_k',
    'chnclear',
    'chnexport',
    'chnget',
    'chnmix',
    'chnparams',
    'chnset',
    'chuap',
   #'cigoto',
   #'cingoto',
   #'ckgoto',
    'clear',
    'clfilt',
    'clip',
    'clockoff',
    'clockon',
    'cmplxprod',
   #'cngoto',
   #'cnkgoto',
    'comb',
    'combinv',
    'compilecsd',
    'compileorc',
    'compilestr',
    'compress',
    'compress2',
    'connect',
    'control',
    'convle',
    'convolve',
    'copya2ftab',
    'copyf2array',
    'cos',
    'cosh',
    'cosinv',
    'cosseg',
    'cossegb',
    'cossegr',
    'cps2pch',
    'cpsmidi',
    'cpsmidib',
    'cpsmidinn',
    'cpsoct',
    'cpspch',
    'cpstmid',
    'cpstun',
    'cpstuni',
    'cpsxpch',
    'cpuprc',
    'cross2',
    'crossfm',
    'crossfmi',
    'crossfmpm',
    'crossfmpmi',
    'crosspm',
    'crosspmi',
    'crunch',
    'ctlchn',
    'ctrl14',
    'ctrl21',
    'ctrl7',
    'ctrlinit',
    'cuserrnd',
    'dam',
    'date',
    'dates',
    'db',
    'dbamp',
    'dbfsamp',
    'dcblock',
    'dcblock2',
    'dconv',
    'dct',
    'dctinv',
    'delay',
    'delay1',
    'delayk',
    'delayr',
    'delayw',
    'deltap',
    'deltap3',
    'deltapi',
    'deltapn',
    'deltapx',
    'deltapxw',
    'denorm',
    'diff',
    'directory',
    'diskgrain',
    'diskin',
    'diskin2',
    'dispfft',
    'display',
    'distort',
    'distort1',
    'divz',
    'doppler',
    'downsamp',
    'dripwater',
    'dumpk',
    'dumpk2',
    'dumpk3',
    'dumpk4',
    'duserrnd',
    'dust',
    'dust2',
   #'endin',
   #'endop',
    'envlpx',
    'envlpxr',
    'ephasor',
    'eqfil',
    'evalstr',
    'event',
    'event_i',
    'exciter',
    'exitnow',
    'exp',
    'expcurve',
    'expon',
    'exprand',
    'exprandi',
    'expseg',
    'expsega',
    'expsegb',
    'expsegba',
    'expsegr',
    'fareylen',
    'fareyleni',
    'faustaudio',
    'faustcompile',
    'faustctl',
    'faustgen',
    'fft',
    'fftinv',
    'ficlose',
    'filebit',
    'filelen',
    'filenchnls',
    'filepeak',
    'filescal',
    'filesr',
    'filevalid',
    'fillarray',
    'filter2',
    'fin',
    'fini',
    'fink',
    'fiopen',
    'flanger',
    'flashtxt',
    'flooper',
    'flooper2',
    'floor',
    'fluidAllOut',
    'fluidCCi',
    'fluidCCk',
    'fluidControl',
    'fluidEngine',
    'fluidLoad',
    'fluidNote',
    'fluidOut',
    'fluidProgramSelect',
    'fluidSetInterpMethod',
    'fmb3',
    'fmbell',
    'fmmetal',
    'fmpercfl',
    'fmrhode',
    'fmvoice',
    'fmwurlie',
    'fof',
    'fof2',
    'fofilter',
    'fog',
    'fold',
    'follow',
    'follow2',
    'foscil',
    'foscili',
    'fout',
    'fouti',
    'foutir',
    'foutk',
    'fprintks',
    'fprints',
    'frac',
    'fractalnoise',
    'framebuffer',
    'freeverb',
    'ftchnls',
    'ftconv',
    'ftcps',
    'ftfree',
    'ftgen',
    'ftgenonce',
    'ftgentmp',
    'ftlen',
    'ftload',
    'ftloadk',
    'ftlptim',
    'ftmorf',
    'ftresize',
    'ftresizei',
    'ftsamplebank',
    'ftsave',
    'ftsavek',
    'ftsr',
    'gain',
    'gainslider',
    'gauss',
    'gaussi',
    'gausstrig',
    'gbuzz',
    'genarray',
    'genarray_i',
    'gendy',
    'gendyc',
    'gendyx',
    'getcfg',
    'getcol',
    'getftargs',
    'getrow',
    'getseed',
    'gogobel',
   #'goto',
    'grain',
    'grain2',
    'grain3',
    'granule',
    'guiro',
    'harmon',
    'harmon2',
    'harmon3',
    'harmon4',
    'hdf5read',
    'hdf5write',
    'hilbert',
    'hrtfearly',
    'hrtfmove',
    'hrtfmove2',
    'hrtfreverb',
    'hrtfstat',
    'hsboscil',
    'hvs1',
    'hvs2',
    'hvs3',
    'i',
   #'igoto',
    'ihold',
    'imagecreate',
    'imagefree',
    'imagegetpixel',
    'imageload',
    'imagesave',
    'imagesetpixel',
    'imagesize',
    'in',
    'in32',
    'inch',
    'inh',
    'init',
    'initc14',
    'initc21',
    'initc7',
    'inleta',
    'inletf',
    'inletk',
    'inletkid',
    'inletv',
    'ino',
    'inq',
    'inrg',
    'ins',
    'insglobal',
    'insremot',
   #'instr',
    'int',
    'integ',
    'interp',
    'invalue',
    'inx',
    'inz',
    'jitter',
    'jitter2',
    'jspline',
    'k',
   #'kgoto',
    'lenarray',
    'lfo',
    'limit',
    'line',
    'linen',
    'linenr',
    'lineto',
    'linrand',
    'linseg',
    'linsegb',
    'linsegr',
    'locsend',
    'locsig',
    'log',
    'log10',
    'log2',
    'logbtwo',
    'logcurve',
   #'loop_ge',
   #'loop_gt',
   #'loop_le',
   #'loop_lt',
    'loopseg',
    'loopsegp',
    'looptseg',
    'loopxseg',
    'lorenz',
    'loscil',
    'loscil3',
    'loscilx',
    'lowpass2',
    'lowres',
    'lowresx',
    'lpf18',
    'lpform',
    'lpfreson',
    'lphasor',
    'lpinterp',
    'lposcil',
    'lposcil3',
    'lposcila',
    'lposcilsa',
    'lposcilsa2',
    'lpread',
    'lpreson',
    'lpshold',
    'lpsholdp',
    'lpslot',
    'lua_exec',
    'lua_ikopcall',
    'lua_opdef',
    'mac',
    'maca',
    'madsr',
    'mags',
    'mandel',
    'mandol',
    'maparray',
    'maparray_i',
    'marimba',
    'massign',
    'max',
    'max_k',
    'maxabs',
    'maxabsaccum',
    'maxaccum',
    'maxalloc',
    'maxarray',
    'mclock',
    'mdelay',
    'median',
    'mediank',
    'metro',
    'mfb',
    'midglobal',
    'midic14',
    'midic21',
    'midic7',
    'midichannelaftertouch',
    'midichn',
    'midicontrolchange',
    'midictrl',
    'mididefault',
    'midifilestatus',
    'midiin',
    'midinoteoff',
    'midinoteoncps',
    'midinoteonkey',
    'midinoteonoct',
    'midinoteonpch',
    'midion',
    'midion2',
    'midiout',
    'midipgm',
    'midipitchbend',
    'midipolyaftertouch',
    'midiprogramchange',
    'miditempo',
    'midremot',
    'min',
    'minabs',
    'minabsaccum',
    'minaccum',
    'minarray',
    'mincer',
    'mirror',
    'mode',
    'modmatrix',
    'monitor',
    'moog',
    'moogladder',
    'moogladder2',
    'moogvcf',
    'moogvcf2',
    'moscil',
    'mp3bitrate',
    'mp3in',
    'mp3len',
    'mp3nchnls',
    'mp3scal',
    'mp3sr',
    'mpulse',
    'mrtmsg',
    'multitap',
    'mute',
    'mvchpf',
    'mvclpf1',
    'mvclpf2',
    'mvclpf3',
    'mvclpf4',
    'mxadsr',
    'nchnls_hw',
    'nestedap',
    'nlalp',
    'nlfilt',
    'nlfilt2',
    'noise',
    'noteoff',
    'noteon',
    'noteondur',
    'noteondur2',
    'notnum',
    'nreverb',
    'nrpn',
    'nsamp',
    'nstance',
    'nstrnum',
    'ntrpol',
    'nxtpow2',
    'octave',
    'octcps',
    'octmidi',
    'octmidib',
    'octmidinn',
    'octpch',
    'olabuffer',
   #'opcode',
    'oscbnk',
    'oscil',
    'oscil1',
    'oscil1i',
    'oscil3',
    'oscili',
    'oscilikt',
    'osciliktp',
    'oscilikts',
    'osciln',
    'oscils',
    'oscilx',
    'out',
    'out32',
    'outc',
    'outch',
    'outh',
    'outiat',
    'outic',
    'outic14',
    'outipat',
    'outipb',
    'outipc',
    'outkat',
    'outkc',
    'outkc14',
    'outkpat',
    'outkpb',
    'outkpc',
    'outleta',
    'outletf',
    'outletk',
    'outletkid',
    'outletv',
    'outo',
    'outq',
    'outq1',
    'outq2',
    'outq3',
    'outq4',
    'outrg',
    'outs',
    'outs1',
    'outs2',
    'outvalue',
    'outx',
    'outz',
    'p',
    'pan',
    'pan2',
    'pareq',
    'part2txt',
    'partials',
    'partikkel',
    'partikkelget',
    'partikkelset',
    'partikkelsync',
    'passign',
    'paulstretch',
    'pcauchy',
    'pchbend',
    'pchmidi',
    'pchmidib',
    'pchmidinn',
    'pchoct',
    'pconvolve',
    'pcount',
    'pdclip',
    'pdhalf',
    'pdhalfy',
    'peak',
    'pgmassign',
    'pgmchn',
    'phaser1',
    'phaser2',
    'phasor',
    'phasorbnk',
    'phs',
    'pindex',
    'pinker',
    'pinkish',
    'pitch',
    'pitchac',
    'pitchamdf',
    'planet',
    'platerev',
    'plltrack',
    'pluck',
    'poisson',
    'pol2rect',
    'polyaft',
    'polynomial',
    'port',
    'portk',
    'poscil',
    'poscil3',
    'pow',
    'powershape',
    'powoftwo',
    'pows',
    'prealloc',
    'prepiano',
    'print',
    'print_type',
    'printf',
    'printf_i',
    'printk',
    'printk2',
    'printks',
    'printks2',
    'prints',
    'product',
    'pset',
    'ptable',
    'ptable3',
    'ptablei',
    'ptableiw',
    'ptablew',
    'ptrack',
    'puts',
    'pvadd',
    'pvbufread',
    'pvcross',
    'pvinterp',
    'pvoc',
    'pvread',
    'pvs2array',
    'pvs2tab',
    'pvsadsyn',
    'pvsanal',
    'pvsarp',
    'pvsbandp',
    'pvsbandr',
    'pvsbin',
    'pvsblur',
    'pvsbuffer',
    'pvsbufread',
    'pvsbufread2',
    'pvscale',
    'pvscent',
    'pvsceps',
    'pvscross',
    'pvsdemix',
    'pvsdiskin',
    'pvsdisp',
    'pvsenvftw',
    'pvsfilter',
    'pvsfread',
    'pvsfreeze',
    'pvsfromarray',
    'pvsftr',
    'pvsftw',
    'pvsfwrite',
    'pvsgain',
    'pvsgendy',
    'pvshift',
    'pvsifd',
    'pvsin',
    'pvsinfo',
    'pvsinit',
    'pvslock',
    'pvsmaska',
    'pvsmix',
    'pvsmooth',
    'pvsmorph',
    'pvsosc',
    'pvsout',
    'pvspitch',
    'pvstanal',
    'pvstencil',
    'pvsvoc',
    'pvswarp',
    'pvsynth',
    'pwd',
    'pyassign',
    'pyassigni',
    'pyassignt',
    'pycall',
    'pycall1',
    'pycall1i',
    'pycall1t',
    'pycall2',
    'pycall2i',
    'pycall2t',
    'pycall3',
    'pycall3i',
    'pycall3t',
    'pycall4',
    'pycall4i',
    'pycall4t',
    'pycall5',
    'pycall5i',
    'pycall5t',
    'pycall6',
    'pycall6i',
    'pycall6t',
    'pycall7',
    'pycall7i',
    'pycall7t',
    'pycall8',
    'pycall8i',
    'pycall8t',
    'pycalli',
    'pycalln',
    'pycallni',
    'pycallt',
    'pyeval',
    'pyevali',
    'pyevalt',
    'pyexec',
    'pyexeci',
    'pyexect',
    'pyinit',
    'pylassign',
    'pylassigni',
    'pylassignt',
    'pylcall',
    'pylcall1',
    'pylcall1i',
    'pylcall1t',
    'pylcall2',
    'pylcall2i',
    'pylcall2t',
    'pylcall3',
    'pylcall3i',
    'pylcall3t',
    'pylcall4',
    'pylcall4i',
    'pylcall4t',
    'pylcall5',
    'pylcall5i',
    'pylcall5t',
    'pylcall6',
    'pylcall6i',
    'pylcall6t',
    'pylcall7',
    'pylcall7i',
    'pylcall7t',
    'pylcall8',
    'pylcall8i',
    'pylcall8t',
    'pylcalli',
    'pylcalln',
    'pylcallni',
    'pylcallt',
    'pyleval',
    'pylevali',
    'pylevalt',
    'pylexec',
    'pylexeci',
    'pylexect',
    'pylrun',
    'pylruni',
    'pylrunt',
    'pyrun',
    'pyruni',
    'pyrunt',
    'qinf',
    'qnan',
    'r2c',
    'rand',
    'randh',
    'randi',
    'random',
    'randomh',
    'randomi',
    'rbjeq',
    'readclock',
    'readf',
    'readfi',
    'readk',
    'readk2',
    'readk3',
    'readk4',
    'readks',
    'readscore',
    'readscratch',
    'rect2pol',
    'reinit',
    'release',
    'remoteport',
    'remove',
    'repluck',
    'reson',
    'resonk',
    'resonr',
    'resonx',
    'resonxk',
    'resony',
    'resonz',
    'resyn',
   #'return',
    'reverb',
    'reverb2',
    'reverbsc',
    'rewindscore',
    'rezzy',
    'rfft',
    'rifft',
   #'rigoto',
   #'rireturn',
    'rms',
    'rnd',
    'rnd31',
    'round',
    'rspline',
    'rtclock',
    's16b14',
    's32b14',
    'samphold',
    'sandpaper',
    'scale',
    'scalearray',
    'scanhammer',
    'scans',
    'scantable',
    'scanu',
    'schedkwhen',
    'schedkwhennamed',
    'schedule',
    'schedwhen',
    'scoreline',
    'scoreline_i',
    'seed',
    'sekere',
    'semitone',
    'sense',
    'sensekey',
    'seqtime',
    'seqtime2',
    'serialBegin',
    'serialEnd',
    'serialFlush',
    'serialPrint',
    'serialRead',
    'serialWrite',
    'serialWrite_i',
    'setcol',
    'setctrl',
    'setksmps',
    'setrow',
    'setscorepos',
    'sfilist',
    'sfinstr',
    'sfinstr3',
    'sfinstr3m',
    'sfinstrm',
    'sfload',
    'sflooper',
    'sfpassign',
    'sfplay',
    'sfplay3',
    'sfplay3m',
    'sfplaym',
    'sfplist',
    'sfpreset',
    'shaker',
    'shiftin',
    'shiftout',
    'signalflowgraph',
    'signum',
    'sin',
    'sinh',
    'sininv',
    'sinsyn',
    'sleighbells',
    'slicearray',
    'slider16',
    'slider16f',
    'slider16table',
    'slider16tablef',
    'slider32',
    'slider32f',
    'slider32table',
    'slider32tablef',
    'slider64',
    'slider64f',
    'slider64table',
    'slider64tablef',
    'slider8',
    'slider8f',
    'slider8table',
    'slider8tablef',
    'sliderKawai',
    'sndloop',
    'sndwarp',
    'sndwarpst',
    'sockrecv',
    'sockrecvs',
    'socksend',
    'socksends',
    'soundin',
    'space',
    'spat3d',
    'spat3di',
    'spat3dt',
    'spdist',
    'splitrig',
    'sprintf',
    'sprintfk',
    'spsend',
    'sqrt',
    'statevar',
    'stix',
    'strcat',
    'strcatk',
    'strchar',
    'strchark',
    'strcmp',
    'strcmpk',
    'strcpy',
    'strcpyk',
    'strecv',
    'streson',
    'strfromurl',
    'strget',
    'strindex',
    'strindexk',
    'strlen',
    'strlenk',
    'strlower',
    'strlowerk',
    'strrindex',
    'strrindexk',
    'strset',
    'strsub',
    'strsubk',
    'strtod',
    'strtodk',
    'strtol',
    'strtolk',
    'strupper',
    'strupperk',
    'stsend',
    'subinstr',
    'subinstrinit',
    'sum',
    'sumarray',
    'svfilter',
    'syncgrain',
    'syncloop',
    'syncphasor',
    'system',
    'system_i',
    'tab',
    'tab2pvs',
    'tab_i',
    'tabifd',
    'table',
    'table3',
    'table3kt',
    'tablecopy',
    'tablefilter',
    'tablefilteri',
    'tablegpw',
    'tablei',
    'tableicopy',
    'tableigpw',
    'tableikt',
    'tableimix',
    'tableiw',
    'tablekt',
    'tablemix',
    'tableng',
    'tablera',
    'tableseg',
    'tableshuffle',
    'tableshufflei',
    'tablew',
    'tablewa',
    'tablewkt',
    'tablexkt',
    'tablexseg',
    'tabmorph',
    'tabmorpha',
    'tabmorphak',
    'tabmorphi',
    'tabplay',
    'tabrec',
    'tabsum',
    'tabw',
    'tabw_i',
    'tambourine',
    'tan',
    'tanh',
    'taninv',
    'taninv2',
    'tb0',
    'tb0_init',
    'tb1',
    'tb10',
    'tb10_init',
    'tb11',
    'tb11_init',
    'tb12',
    'tb12_init',
    'tb13',
    'tb13_init',
    'tb14',
    'tb14_init',
    'tb15',
    'tb15_init',
    'tb1_init',
    'tb2',
    'tb2_init',
    'tb3',
    'tb3_init',
    'tb4',
    'tb4_init',
    'tb5',
    'tb5_init',
    'tb6',
    'tb6_init',
    'tb7',
    'tb7_init',
    'tb8',
    'tb8_init',
    'tb9',
    'tb9_init',
    'tbvcf',
    'tempest',
    'tempo',
    'temposcal',
    'tempoval',
   #'tigoto',
    'timedseq',
    'timeinstk',
    'timeinsts',
    'timek',
    'times',
   #'timout',
    'tival',
    'tlineto',
    'tone',
    'tonek',
    'tonex',
    'tradsyn',
    'trandom',
    'transeg',
    'transegb',
    'transegr',
    'trcross',
    'trfilter',
    'trhighest',
    'trigger',
    'trigseq',
    'trirand',
    'trlowest',
    'trmix',
    'trscale',
    'trshift',
    'trsplit',
    'turnoff',
    'turnoff2',
    'turnon',
    'unirand',
    'unwrap',
    'upsamp',
    'urandom',
    'urd',
    'vactrol',
    'vadd',
    'vadd_i',
    'vaddv',
    'vaddv_i',
    'vaget',
    'valpass',
    'vaset',
    'vbap',
    'vbapg',
    'vbapgmove',
    'vbaplsinit',
    'vbapmove',
    'vbapz',
    'vbapzmove',
    'vcella',
    'vco',
    'vco2',
    'vco2ft',
    'vco2ift',
    'vco2init',
    'vcomb',
    'vcopy',
    'vcopy_i',
    'vdel_k',
    'vdelay',
    'vdelay3',
    'vdelayk',
    'vdelayx',
    'vdelayxq',
    'vdelayxs',
    'vdelayxw',
    'vdelayxwq',
    'vdelayxws',
    'vdivv',
    'vdivv_i',
    'vecdelay',
    'veloc',
    'vexp',
    'vexp_i',
    'vexpseg',
    'vexpv',
    'vexpv_i',
    'vibes',
    'vibr',
    'vibrato',
    'vincr',
    'vlimit',
    'vlinseg',
    'vlowres',
    'vmap',
    'vmirror',
    'vmult',
    'vmult_i',
    'vmultv',
    'vmultv_i',
    'voice',
    'vosim',
    'vphaseseg',
    'vport',
    'vpow',
    'vpow_i',
    'vpowv',
    'vpowv_i',
    'vpvoc',
    'vrandh',
    'vrandi',
    'vsubv',
    'vsubv_i',
    'vtaba',
    'vtabi',
    'vtabk',
    'vtable1k',
    'vtablea',
    'vtablei',
    'vtablek',
    'vtablewa',
    'vtablewi',
    'vtablewk',
    'vtabwa',
    'vtabwi',
    'vtabwk',
    'vwrap',
    'waveset',
    'weibull',
    'wgbow',
    'wgbowedbar',
    'wgbrass',
    'wgclar',
    'wgflute',
    'wgpluck',
    'wgpluck2',
    'wguide1',
    'wguide2',
    'wiiconnect',
    'wiidata',
    'wiirange',
    'wiisend',
    'window',
    'wrap',
    'writescratch',
    'wterrain',
    'xadsr',
    'xin',
    'xout',
    'xscanmap',
    'xscans',
    'xscansmap',
    'xscanu',
    'xtratim',
    'zacl',
    'zakinit',
    'zamod',
    'zar',
    'zarg',
    'zaw',
    'zawm',
    'zfilter2',
    'zir',
    'ziw',
    'ziwm',
    'zkcl',
    'zkmod',
    'zkr',
    'zkw',
    'zkwm'
))

DEPRECATED_OPCODES = set((
    'array',
    'bformdec',
    'bformenc',
    'copy2ftab',
    'copy2ttab',
    'hrtfer',
    'ktableseg',
    'lentab',
    'maxtab',
    'mintab',
    'pop',
    'pop_f',
    'push',
    'push_f',
    'scalet',
    'sndload',
    'soundout',
    'soundouts',
    'specaddm',
    'specdiff',
    'specdisp',
    'specfilt',
    'spechist',
    'specptrk',
    'specscal',
    'specsum',
    'spectrum',
    'stack',
    'sumtab',
    'tabgen',
    'tabmap',
    'tabmap_i',
    'tabslice',
    'vbap16',
    'vbap4',
    'vbap4move',
    'vbap8',
    'vbap8move',
    'xyin'
))
