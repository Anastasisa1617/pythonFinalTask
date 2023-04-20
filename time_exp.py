#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Март 18, 2023, at 22:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'time_exp'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=expInfo, runtimeInfo=None,
                                 originPath='C:\\PSYCHOPY EXPERIMENTS\\my experiments\\timeEstimation\\time_exp.py',
                                 savePickle=True, saveWideText=True,
                                 dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "instr"
instrClock = core.Clock()
instrtrain = visual.TextStim(win=win, name='instrtrain',
                             text='Это тренировочный блок. \nСейчас вам будут показаны эталонные стимулы двух длительностей: длинные и короткий. Стимулы будут показаны в хаотичном порядке. Ваша задача — запомнить их длительность. Ничего делать не нужно, просто смотрите на экран. \nКогда будете готовы — скажите "готов/а"',
                             font='Open Sans',
                             pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
instrtrain_stop = type('', (), {})()  # Create an object to use as a name space
instrtrain_stop.device = None
instrtrain_stop.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        instrtrain_stop.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        instrtrain_stop.device = joystickCache[0]
    else:
        instrtrain_stop.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(instrtrain_stop.device_number))
except Exception:
    pass

if not instrtrain_stop.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

instrtrain_stop.status = None
instrtrain_stop.clock = core.Clock()
instrtrain_stop.numButtons = instrtrain_stop.device.getNumButtons()

# Initialize components for Routine "mask"
maskClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text='+',
                       font='Open Sans',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
train_stim = visual.Rect(
    win=win, name='train_stim',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "instrtwo"
instrtwoClock = core.Clock()
instrtrial = visual.TextStim(win=win, name='instrtrial',
                             text='Это экспериментальный блок :)\nСейчас на экране будут показаны стимулы разной длительности. Ваша задача — определить, стимул по продолжительности ближе к длинному или короткому эталонному стимулу, которые были показаны ранее. Ответ нужно давать вслух: если ближе к короткому — говорите “короткий”, если к длинному — “длинный”. Не задумывайтесь над ответом долго, на каждый ответ у вас будет 2 секунды. \nКогда будете готовы — скажите "готов/а"',
                             font='Open Sans',
                             pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                             color='white', colorSpace='rgb', opacity=None,
                             languageStyle='LTR',
                             depth=0.0);
button_resp = type('', (), {})()  # Create an object to use as a name space
button_resp.device = None
button_resp.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp.device = joystickCache[0]
    else:
        button_resp.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp.device_number))
except Exception:
    pass

if not button_resp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp.status = None
button_resp.clock = core.Clock()
button_resp.numButtons = button_resp.device.getNumButtons()

# Initialize components for Routine "mask"
maskClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text='+',
                       font='Open Sans',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_stim = visual.Rect(
    win=win, name='trial_stim',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "responce"
responceClock = core.Clock()
trial_resp = type('', (), {})()  # Create an object to use as a name space
trial_resp.device = None
trial_resp.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        trial_resp.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        trial_resp.device = joystickCache[0]
    else:
        trial_resp.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(trial_resp.device_number))
except Exception:
    pass

if not trial_resp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

trial_resp.status = None
trial_resp.clock = core.Clock()
trial_resp.numButtons = trial_resp.device.getNumButtons()

text_resp_short = visual.TextStim(win=win, name='text_resp_short',
                                  text='ближе к короткому ',
                                  font='Open Sans',
                                  pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=-1.0);
text_resp_long = visual.TextStim(win=win, name='text_resp_long',
                                 text='ближе к длинному',
                                 font='Open Sans',
                                 pos=(0.5, 0), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=None,
                                 languageStyle='LTR',
                                 depth=-2.0);

# Initialize components for Routine "instrthree"
instrthreeClock = core.Clock()
instrtrain_stop_2 = type('', (), {})()  # Create an object to use as a name space
instrtrain_stop_2.device = None
instrtrain_stop_2.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        instrtrain_stop_2.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        instrtrain_stop_2.device = joystickCache[0]
    else:
        instrtrain_stop_2.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(instrtrain_stop_2.device_number))
except Exception:
    pass

if not instrtrain_stop_2.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

instrtrain_stop_2.status = None
instrtrain_stop_2.clock = core.Clock()
instrtrain_stop_2.numButtons = instrtrain_stop_2.device.getNumButtons()

instrtrain_two = visual.TextStim(win=win, name='instrtrain_two',
                                 text='Сейчас вам снова будут показаны эталонные стимулы двух длительностей: длинные и короткий. Стимулы будут показаны в хаотичном порядке. Ваша задача — запомнить их длительность. Ничего делать не нужно, просто смотрите на экран. \nКогда будете готовы — скажите "готов/а"',
                                 font='Open Sans',
                                 pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=None,
                                 languageStyle='LTR',
                                 depth=-1.0);

# Initialize components for Routine "mask"
maskClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text='+',
                       font='Open Sans',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "training"
trainingClock = core.Clock()
train_stim = visual.Rect(
    win=win, name='train_stim',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "instrfour"
instrfourClock = core.Clock()
instrfour_stop = type('', (), {})()  # Create an object to use as a name space
instrfour_stop.device = None
instrfour_stop.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        instrfour_stop.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        instrfour_stop.device = joystickCache[0]
    else:
        instrfour_stop.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(instrfour_stop.device_number))
except Exception:
    pass

if not instrfour_stop.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

instrfour_stop.status = None
instrfour_stop.clock = core.Clock()
instrfour_stop.numButtons = instrfour_stop.device.getNumButtons()

text_instrfour = visual.TextStim(win=win, name='text_instrfour',
                                 text='Снова экспериментальный блок :)\nСейчас на экране будут показаны стимулы разной длительности. Ваша задача — определить, стимул по продолжительности ближе к длинному или короткому эталонному стимулу, которые были показаны ранее. Ответ нужно давать вслух: если ближе к короткому — говорите “короткий”, если к длинному — “длинный”. Не задумывайтесь над ответом долго, на каждый ответ у вас будет 2 секунды. \nКогда будете готовы — скажите "готов/а"',
                                 font='Open Sans',
                                 pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=None,
                                 languageStyle='LTR',
                                 depth=-1.0);

# Initialize components for Routine "mask"
maskClock = core.Clock()
text = visual.TextStim(win=win, name='text',
                       text='+',
                       font='Open Sans',
                       pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0,
                       color='white', colorSpace='rgb', opacity=None,
                       languageStyle='LTR',
                       depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_stim = visual.Rect(
    win=win, name='trial_stim',
    width=(0.5, 0.5)[0], height=(0.5, 0.5)[1],
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0, colorSpace='rgb', lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "responce"
responceClock = core.Clock()
trial_resp = type('', (), {})()  # Create an object to use as a name space
trial_resp.device = None
trial_resp.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        trial_resp.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache = {}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        trial_resp.device = joystickCache[0]
    else:
        trial_resp.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning(
            "joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(trial_resp.device_number))
except Exception:
    pass

if not trial_resp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

trial_resp.status = None
trial_resp.clock = core.Clock()
trial_resp.numButtons = trial_resp.device.getNumButtons()

text_resp_short = visual.TextStim(win=win, name='text_resp_short',
                                  text='ближе к короткому ',
                                  font='Open Sans',
                                  pos=(-0.5, 0), height=0.05, wrapWidth=None, ori=0.0,
                                  color='white', colorSpace='rgb', opacity=None,
                                  languageStyle='LTR',
                                  depth=-1.0);
text_resp_long = visual.TextStim(win=win, name='text_resp_long',
                                 text='ближе к длинному',
                                 font='Open Sans',
                                 pos=(0.5, 0), height=0.05, wrapWidth=None, ori=0.0,
                                 color='white', colorSpace='rgb', opacity=None,
                                 languageStyle='LTR',
                                 depth=-2.0);

# Initialize components for Routine "goodbye"
goodbyeClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
                      text='Эксперимент окончен! \nСпасибо за помощь в получении новых знаний о мире :) \n',
                      font='Open Sans',
                      pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                      color='white', colorSpace='rgb', opacity=None,
                      languageStyle='LTR',
                      depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
instrtrain_stop.oldButtonState = instrtrain_stop.device.getAllButtons()[:]
instrtrain_stop.keys = []
instrtrain_stop.rt = []
# keep track of which components have finished
instrComponents = [instrtrain, instrtrain_stop]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrtrain* updates
    if instrtrain.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instrtrain.frameNStart = frameN  # exact frame index
        instrtrain.tStart = t  # local t and not account for scr refresh
        instrtrain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrtrain, 'tStartRefresh')  # time at next scr refresh
        instrtrain.setAutoDraw(True)

    # *instrtrain_stop* updates
    if instrtrain_stop.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instrtrain_stop.frameNStart = frameN  # exact frame index
        instrtrain_stop.tStart = t  # local t and not account for scr refresh
        instrtrain_stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrtrain_stop, 'tStartRefresh')  # time at next scr refresh
        instrtrain_stop.status = STARTED
        # joyButtons checking is just starting
        win.callOnFlip(instrtrain_stop.clock.reset)  # t=0 on next screen flip
    if instrtrain_stop.status == STARTED:
        instrtrain_stop.newButtonState = instrtrain_stop.device.getAllButtons()[:]
        instrtrain_stop.pressedButtons = []
        instrtrain_stop.releasedButtons = []
        instrtrain_stop.newPressedButtons = []
        if instrtrain_stop.newButtonState != instrtrain_stop.oldButtonState:
            instrtrain_stop.pressedButtons = [i for i in range(instrtrain_stop.numButtons) if
                                              instrtrain_stop.newButtonState[i] and not instrtrain_stop.oldButtonState[
                                                  i]]
            instrtrain_stop.releasedButtons = [i for i in range(instrtrain_stop.numButtons) if
                                               not instrtrain_stop.newButtonState[i] and instrtrain_stop.oldButtonState[
                                                   i]]
            instrtrain_stop.oldButtonState = instrtrain_stop.newButtonState
            instrtrain_stop.newPressedButtons = [i for i in [4] if i in instrtrain_stop.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(instrtrain_stop.device_number, i)) for i in
             instrtrain_stop.pressedButtons]
        theseKeys = instrtrain_stop.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            instrtrain_stop.keys = theseKeys[-1]  # just the last key pressed
            instrtrain_stop.rt = instrtrain_stop.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instrtrain_stop.keys in ['', [], None]:  # No response was made
    instrtrain_stop.keys = None
thisExp.addData('instrtrain_stop.keys', instrtrain_stop.keys)
if instrtrain_stop.keys != None:  # we had a response
    thisExp.addData('instrtrain_stop.rt', instrtrain_stop.rt)
thisExp.nextEntry()
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='fullRandom',
                           extraInfo=expInfo, originPath=-1,
                           trialList=data.importConditions('stim_train.xlsx'),
                           seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))

    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [text]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "training"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    trainingComponents = [train_stim]
    for thisComponent in trainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "training"-------
    while continueRoutine:
        # get current time
        t = trainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *train_stim* updates
        if train_stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            train_stim.frameNStart = frameN  # exact frame index
            train_stim.tStart = t  # local t and not account for scr refresh
            train_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_stim, 'tStartRefresh')  # time at next scr refresh
            train_stim.setAutoDraw(True)
        if train_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_stim.tStartRefresh + train_time - frameTolerance:
                # keep track of stop time/frame for later
                train_stim.tStop = t  # not accounting for scr refresh
                train_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_stim, 'tStopRefresh')  # time at next scr refresh
                train_stim.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "training"-------
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('stim_trial.xlsx'),
                             seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))

    # ------Prepare to start Routine "instrtwo"-------
    continueRoutine = True
    # update component parameters for each repeat
    button_resp.oldButtonState = button_resp.device.getAllButtons()[:]
    button_resp.keys = []
    button_resp.rt = []
    # keep track of which components have finished
    instrtwoComponents = [instrtrial, button_resp]
    for thisComponent in instrtwoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrtwoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "instrtwo"-------
    while continueRoutine:
        # get current time
        t = instrtwoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrtwoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instrtrial* updates
        if instrtrial.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            instrtrial.frameNStart = frameN  # exact frame index
            instrtrial.tStart = t  # local t and not account for scr refresh
            instrtrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instrtrial, 'tStartRefresh')  # time at next scr refresh
            instrtrial.setAutoDraw(True)

        # *button_resp* updates
        if button_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            button_resp.frameNStart = frameN  # exact frame index
            button_resp.tStart = t  # local t and not account for scr refresh
            button_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_resp, 'tStartRefresh')  # time at next scr refresh
            button_resp.status = STARTED
            # joyButtons checking is just starting
            win.callOnFlip(button_resp.clock.reset)  # t=0 on next screen flip
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if
                                              button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if
                                               not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [4] if i in button_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(button_resp.device_number, i)) for i in
                 button_resp.pressedButtons]
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:  # at least one key was pressed
                button_resp.keys = theseKeys[-1]  # just the last key pressed
                button_resp.rt = button_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrtwoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instrtwo"-------
    for thisComponent in instrtwoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if button_resp.keys in ['', [], None]:  # No response was made
        button_resp.keys = None
    trials_5.addData('button_resp.keys', button_resp.keys)
    if button_resp.keys != None:  # we had a response
        trials_5.addData('button_resp.rt', button_resp.rt)
    # the Routine "instrtwo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials_5'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=5.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('stim_trial.xlsx'),
                             seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [text]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [trial_stim]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_stim* updates
        if trial_stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            trial_stim.frameNStart = frameN  # exact frame index
            trial_stim.tStart = t  # local t and not account for scr refresh
            trial_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_stim, 'tStartRefresh')  # time at next scr refresh
            trial_stim.setAutoDraw(True)
        if trial_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_stim.tStartRefresh + trial_time - frameTolerance:
                # keep track of stop time/frame for later
                trial_stim.tStop = t  # not accounting for scr refresh
                trial_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_stim, 'tStopRefresh')  # time at next scr refresh
                trial_stim.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "responce"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_resp.oldButtonState = trial_resp.device.getAllButtons()[:]
    trial_resp.keys = []
    trial_resp.rt = []
    # keep track of which components have finished
    responceComponents = [trial_resp, text_resp_short, text_resp_long]
    for thisComponent in responceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "responce"-------
    while continueRoutine:
        # get current time
        t = responceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_resp* updates
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # joyButtons checking is just starting
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
        if trial_resp.status == STARTED:
            trial_resp.newButtonState = trial_resp.device.getAllButtons()[:]
            trial_resp.pressedButtons = []
            trial_resp.releasedButtons = []
            trial_resp.newPressedButtons = []
            if trial_resp.newButtonState != trial_resp.oldButtonState:
                trial_resp.pressedButtons = [i for i in range(trial_resp.numButtons) if
                                             trial_resp.newButtonState[i] and not trial_resp.oldButtonState[i]]
                trial_resp.releasedButtons = [i for i in range(trial_resp.numButtons) if
                                              not trial_resp.newButtonState[i] and trial_resp.oldButtonState[i]]
                trial_resp.oldButtonState = trial_resp.newButtonState
                trial_resp.newPressedButtons = [i for i in [4, 1] if i in trial_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(trial_resp.device_number, i)) for i in
                 trial_resp.pressedButtons]
            theseKeys = trial_resp.newPressedButtons
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_resp.keys = theseKeys[-1]  # just the last key pressed
                trial_resp.rt = trial_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # *text_resp_short* updates
        if text_resp_short.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_resp_short.frameNStart = frameN  # exact frame index
            text_resp_short.tStart = t  # local t and not account for scr refresh
            text_resp_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_resp_short, 'tStartRefresh')  # time at next scr refresh
            text_resp_short.setAutoDraw(True)

        # *text_resp_long* updates
        if text_resp_long.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_resp_long.frameNStart = frameN  # exact frame index
            text_resp_long.tStart = t  # local t and not account for scr refresh
            text_resp_long.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_resp_long, 'tStartRefresh')  # time at next scr refresh
            text_resp_long.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "responce"-------
    for thisComponent in responceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
    trials_2.addData('trial_resp.keys', trial_resp.keys)
    if trial_resp.keys != None:  # we had a response
        trials_2.addData('trial_resp.rt', trial_resp.rt)
    # the Routine "responce" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 5.0 repeats of 'trials_2'


# ------Prepare to start Routine "instrthree"-------
continueRoutine = True
# update component parameters for each repeat
instrtrain_stop_2.oldButtonState = instrtrain_stop_2.device.getAllButtons()[:]
instrtrain_stop_2.keys = []
instrtrain_stop_2.rt = []
# keep track of which components have finished
instrthreeComponents = [instrtrain_stop_2, instrtrain_two]
for thisComponent in instrthreeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrthreeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrthree"-------
while continueRoutine:
    # get current time
    t = instrthreeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrthreeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrtrain_stop_2* updates
    if instrtrain_stop_2.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instrtrain_stop_2.frameNStart = frameN  # exact frame index
        instrtrain_stop_2.tStart = t  # local t and not account for scr refresh
        instrtrain_stop_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrtrain_stop_2, 'tStartRefresh')  # time at next scr refresh
        instrtrain_stop_2.status = STARTED
        # joyButtons checking is just starting
        win.callOnFlip(instrtrain_stop_2.clock.reset)  # t=0 on next screen flip
    if instrtrain_stop_2.status == STARTED:
        instrtrain_stop_2.newButtonState = instrtrain_stop_2.device.getAllButtons()[:]
        instrtrain_stop_2.pressedButtons = []
        instrtrain_stop_2.releasedButtons = []
        instrtrain_stop_2.newPressedButtons = []
        if instrtrain_stop_2.newButtonState != instrtrain_stop_2.oldButtonState:
            instrtrain_stop_2.pressedButtons = [i for i in range(instrtrain_stop_2.numButtons) if
                                                instrtrain_stop_2.newButtonState[i] and not
                                                instrtrain_stop_2.oldButtonState[i]]
            instrtrain_stop_2.releasedButtons = [i for i in range(instrtrain_stop_2.numButtons) if
                                                 not instrtrain_stop_2.newButtonState[i] and
                                                 instrtrain_stop_2.oldButtonState[i]]
            instrtrain_stop_2.oldButtonState = instrtrain_stop_2.newButtonState
            instrtrain_stop_2.newPressedButtons = [i for i in [4] if i in instrtrain_stop_2.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(instrtrain_stop_2.device_number, i)) for i in
             instrtrain_stop_2.pressedButtons]
        theseKeys = instrtrain_stop_2.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            instrtrain_stop_2.keys = theseKeys[-1]  # just the last key pressed
            instrtrain_stop_2.rt = instrtrain_stop_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # *instrtrain_two* updates
    if instrtrain_two.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instrtrain_two.frameNStart = frameN  # exact frame index
        instrtrain_two.tStart = t  # local t and not account for scr refresh
        instrtrain_two.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrtrain_two, 'tStartRefresh')  # time at next scr refresh
        instrtrain_two.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrthreeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrthree"-------
for thisComponent in instrthreeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instrtrain_stop_2.keys in ['', [], None]:  # No response was made
    instrtrain_stop_2.keys = None
thisExp.addData('instrtrain_stop_2.keys', instrtrain_stop_2.keys)
if instrtrain_stop_2.keys != None:  # we had a response
    thisExp.addData('instrtrain_stop_2.rt', instrtrain_stop_2.rt)
thisExp.nextEntry()
# the Routine "instrthree" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1.0, method='fullRandom',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('stim_train.xlsx'),
                             seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))

    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [text]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "training"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    trainingComponents = [train_stim]
    for thisComponent in trainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "training"-------
    while continueRoutine:
        # get current time
        t = trainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *train_stim* updates
        if train_stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            train_stim.frameNStart = frameN  # exact frame index
            train_stim.tStart = t  # local t and not account for scr refresh
            train_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(train_stim, 'tStartRefresh')  # time at next scr refresh
            train_stim.setAutoDraw(True)
        if train_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > train_stim.tStartRefresh + train_time - frameTolerance:
                # keep track of stop time/frame for later
                train_stim.tStop = t  # not accounting for scr refresh
                train_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(train_stim, 'tStopRefresh')  # time at next scr refresh
                train_stim.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "training"-------
    for thisComponent in trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'trials_3'


# ------Prepare to start Routine "instrfour"-------
continueRoutine = True
# update component parameters for each repeat
instrfour_stop.oldButtonState = instrfour_stop.device.getAllButtons()[:]
instrfour_stop.keys = []
instrfour_stop.rt = []
# keep track of which components have finished
instrfourComponents = [instrfour_stop, text_instrfour]
for thisComponent in instrfourComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrfourClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instrfour"-------
while continueRoutine:
    # get current time
    t = instrfourClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrfourClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instrfour_stop* updates
    if instrfour_stop.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        instrfour_stop.frameNStart = frameN  # exact frame index
        instrfour_stop.tStart = t  # local t and not account for scr refresh
        instrfour_stop.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrfour_stop, 'tStartRefresh')  # time at next scr refresh
        instrfour_stop.status = STARTED
        # joyButtons checking is just starting
        win.callOnFlip(instrfour_stop.clock.reset)  # t=0 on next screen flip
    if instrfour_stop.status == STARTED:
        instrfour_stop.newButtonState = instrfour_stop.device.getAllButtons()[:]
        instrfour_stop.pressedButtons = []
        instrfour_stop.releasedButtons = []
        instrfour_stop.newPressedButtons = []
        if instrfour_stop.newButtonState != instrfour_stop.oldButtonState:
            instrfour_stop.pressedButtons = [i for i in range(instrfour_stop.numButtons) if
                                             instrfour_stop.newButtonState[i] and not instrfour_stop.oldButtonState[i]]
            instrfour_stop.releasedButtons = [i for i in range(instrfour_stop.numButtons) if
                                              not instrfour_stop.newButtonState[i] and instrfour_stop.oldButtonState[i]]
            instrfour_stop.oldButtonState = instrfour_stop.newButtonState
            instrfour_stop.newPressedButtons = [i for i in [4] if i in instrfour_stop.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(instrfour_stop.device_number, i)) for i in
             instrfour_stop.pressedButtons]
        theseKeys = instrfour_stop.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            instrfour_stop.keys = theseKeys[-1]  # just the last key pressed
            instrfour_stop.rt = instrfour_stop.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # *text_instrfour* updates
    if text_instrfour.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        text_instrfour.frameNStart = frameN  # exact frame index
        text_instrfour.tStart = t  # local t and not account for scr refresh
        text_instrfour.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_instrfour, 'tStartRefresh')  # time at next scr refresh
        text_instrfour.setAutoDraw(True)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrfourComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrfour"-------
for thisComponent in instrfourComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instrfour_stop.keys in ['', [], None]:  # No response was made
    instrfour_stop.keys = None
thisExp.addData('instrfour_stop.keys', instrfour_stop.keys)
if instrfour_stop.keys != None:  # we had a response
    thisExp.addData('instrfour_stop.rt', instrfour_stop.rt)
thisExp.nextEntry()
# the Routine "instrfour" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=5.0, method='random',
                             extraInfo=expInfo, originPath=-1,
                             trialList=data.importConditions('stim_trial.xlsx'),
                             seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))

    # ------Prepare to start Routine "mask"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    maskComponents = [text]
    for thisComponent in maskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "mask"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "mask"-------
    for thisComponent in maskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    trialComponents = [trial_stim]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_stim* updates
        if trial_stim.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            trial_stim.frameNStart = frameN  # exact frame index
            trial_stim.tStart = t  # local t and not account for scr refresh
            trial_stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_stim, 'tStartRefresh')  # time at next scr refresh
            trial_stim.setAutoDraw(True)
        if trial_stim.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trial_stim.tStartRefresh + trial_time - frameTolerance:
                # keep track of stop time/frame for later
                trial_stim.tStop = t  # not accounting for scr refresh
                trial_stim.frameNStop = frameN  # exact frame index
                win.timeOnFlip(trial_stim, 'tStopRefresh')  # time at next scr refresh
                trial_stim.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "responce"-------
    continueRoutine = True
    # update component parameters for each repeat
    trial_resp.oldButtonState = trial_resp.device.getAllButtons()[:]
    trial_resp.keys = []
    trial_resp.rt = []
    # keep track of which components have finished
    responceComponents = [trial_resp, text_resp_short, text_resp_long]
    for thisComponent in responceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    responceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "responce"-------
    while continueRoutine:
        # get current time
        t = responceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=responceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *trial_resp* updates
        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            trial_resp.frameNStart = frameN  # exact frame index
            trial_resp.tStart = t  # local t and not account for scr refresh
            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
            trial_resp.status = STARTED
            # joyButtons checking is just starting
            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
        if trial_resp.status == STARTED:
            trial_resp.newButtonState = trial_resp.device.getAllButtons()[:]
            trial_resp.pressedButtons = []
            trial_resp.releasedButtons = []
            trial_resp.newPressedButtons = []
            if trial_resp.newButtonState != trial_resp.oldButtonState:
                trial_resp.pressedButtons = [i for i in range(trial_resp.numButtons) if
                                             trial_resp.newButtonState[i] and not trial_resp.oldButtonState[i]]
                trial_resp.releasedButtons = [i for i in range(trial_resp.numButtons) if
                                              not trial_resp.newButtonState[i] and trial_resp.oldButtonState[i]]
                trial_resp.oldButtonState = trial_resp.newButtonState
                trial_resp.newPressedButtons = [i for i in [4, 1] if i in trial_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(trial_resp.device_number, i)) for i in
                 trial_resp.pressedButtons]
            theseKeys = trial_resp.newPressedButtons
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_resp.keys = theseKeys[-1]  # just the last key pressed
                trial_resp.rt = trial_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False

        # *text_resp_short* updates
        if text_resp_short.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_resp_short.frameNStart = frameN  # exact frame index
            text_resp_short.tStart = t  # local t and not account for scr refresh
            text_resp_short.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_resp_short, 'tStartRefresh')  # time at next scr refresh
            text_resp_short.setAutoDraw(True)

        # *text_resp_long* updates
        if text_resp_long.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
            # keep track of start time/frame for later
            text_resp_long.frameNStart = frameN  # exact frame index
            text_resp_long.tStart = t  # local t and not account for scr refresh
            text_resp_long.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_resp_long, 'tStartRefresh')  # time at next scr refresh
            text_resp_long.setAutoDraw(True)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "responce"-------
    for thisComponent in responceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_resp.keys in ['', [], None]:  # No response was made
        trial_resp.keys = None
    trials_4.addData('trial_resp.keys', trial_resp.keys)
    if trial_resp.keys != None:  # we had a response
        trials_4.addData('trial_resp.rt', trial_resp.rt)
    # the Routine "responce" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 5.0 repeats of 'trials_4'


# ------Prepare to start Routine "goodbye"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
goodbyeComponents = [bye]
for thisComponent in goodbyeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbyeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = goodbyeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbyeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *bye* updates
    if bye.status == NOT_STARTED and tThisFlip >= 0.0 - frameTolerance:
        # keep track of start time/frame for later
        bye.frameNStart = frameN  # exact frame index
        bye.tStart = t  # local t and not account for scr refresh
        bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    if bye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye.tStartRefresh + 5.0 - frameTolerance:
            # keep track of stop time/frame for later
            bye.tStop = t  # not accounting for scr refresh
            bye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
            bye.setAutoDraw(False)

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbyeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye"-------
for thisComponent in goodbyeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename + '.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()