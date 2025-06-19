
########################################################################
#                          Libraries import                            #

from PySide6.QtCore import Qt
from py_toggle import PyToggle
import Settings
import Page201,Page202



########################################################################
#                         Generate Toggle Buttons                      #
########################################################################

def Buttons(self):

    # Generate toggle buttons for Spikeling Page
    self.ui.PatchClamp_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                               circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                               active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                               )
    self.ui.Noise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                          circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                          active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                          )
    self.ui.PhotoGain_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                              circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                              active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                              )
    self.ui.PhotoDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                               circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                               active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                               )
    self.ui.PhotoRecovery_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                  circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                  active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                  )
    self.ui.StimFre_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                            circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                            active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[5])
                                            )
    self.ui.StimStr_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                            circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                            active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[5])
                                            )
    self.ui.StimCus_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                            circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                            active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[5])
                                            )
    self.ui.Synapse1_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                             circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                             active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[7])
                                             )
    self.ui.Synapse1Decay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                  circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                  active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[7])
                                                  )
    self.ui.Synapse2_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                             circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                             active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                             )
    self.ui.Synapse2Decay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                  circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                  active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                  )
    self.ui.Spikeling_PatchClamp_toggle_layout.addWidget(self.ui.PatchClamp_toggleButton)
    self.ui.Spikeling_PatchClamp_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_Noise_toggle_layout.addWidget(self.ui.Noise_toggleButton)
    self.ui.Spikeling_Noise_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_Synapse1_toggle_layout.addWidget(self.ui.Synapse1_toggleButton)
    self.ui.Spikeling_Synapse1_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_Synapse1_Decay_toggle_layout.addWidget(self.ui.Synapse1Decay_toggleButton)
    self.ui.Spikeling_Synapse1_Decay_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_Synapse2_toggle_layout.addWidget(self.ui.Synapse2_toggleButton)
    self.ui.Spikeling_Synapse2_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_Synapse2_Decay_toggle_layout.addWidget(self.ui.Synapse2Decay_toggleButton)
    self.ui.Spikeling_Synapse2_Decay_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    self.ui.Spikeling_StimFre_toggle_layout.addWidget(self.ui.StimFre_toggleButton)
    self.ui.Spikeling_StimFre_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_StimStr_toggle_layout.addWidget(self.ui.StimStr_toggleButton)
    self.ui.Spikeling_StimStr_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_CustomStimulus_toggle_layout.addWidget(self.ui.StimCus_toggleButton)
    self.ui.Spikeling_CustomStimulus_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_PR_toggle_layout.addWidget(self.ui.PhotoGain_toggleButton)
    self.ui.Spikeling_PR_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Spikeling_PRDecay_Toggle_layout.addWidget(self.ui.PhotoDecay_toggleButton)
    self.ui.Spikeling_PRDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.SpikelingPRRecovery_toggle_layout.addWidget(self.ui.PhotoRecovery_toggleButton)
    self.ui.SpikelingPRRecovery_toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    # Generate toggle buttons for Imaging Page
    self.ui.Imaging_FrameRate_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                      )
    self.ui.Imaging_PMT_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                )
    self.ui.Imaging_Laser_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                  circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                  active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                  )

    self.ui.Imaging_CalciumDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                         circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                         active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                         )
    self.ui.Imaging_CalciumJump_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                        circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                        active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                        )
    self.ui.Imaging_CalciumNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                         circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                         active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                         )
    self.ui.Imaging_CalciumBaseline_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                            circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                            active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                            )

    self.ui.Imaging_kd_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                               circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                               active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                               )
    self.ui.Imaging_Hill_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                 circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                 active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                 )
    self.ui.Imaging_PhotoShotNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                           circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                           active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                           )
    self.ui.Imaging_FluoNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                      )
    self.ui.Imaging_FluoScale_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                      circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                      active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                      )
    self.ui.Imaging_FluoOffset_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                       circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                       active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                       )
    self.ui.Imaging_Saturation_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                       circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                       active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                       )

    self.ui.Imaging_FrameRate_Toggle_layout.addWidget(self.ui.Imaging_FrameRate_toggleButton)
    self.ui.Imaging_FrameRate_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_PMT_Toggle_layout.addWidget(self.ui.Imaging_PMT_toggleButton)
    self.ui.Imaging_PMT_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_Laser_Toggle_layout.addWidget(self.ui.Imaging_Laser_toggleButton)
    self.ui.Imaging_Laser_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    self.ui.Imaging_CalciumDecay_Toggle_layout.addWidget(self.ui.Imaging_CalciumDecay_toggleButton)
    self.ui.Imaging_CalciumDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_CalciumJump_Toggle_layout.addWidget(self.ui.Imaging_CalciumJump_toggleButton)
    self.ui.Imaging_CalciumJump_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_CalciumNoise_Toggle_layout.addWidget(self.ui.Imaging_CalciumNoise_toggleButton)
    self.ui.Imaging_CalciumNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_CalciumBaseline_Toggle_layout.addWidget(self.ui.Imaging_CalciumBaseline_toggleButton)
    self.ui.Imaging_CalciumBaseline_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    self.ui.Imaging_kd_Toggle_layout.addWidget(self.ui.Imaging_kd_toggleButton)
    self.ui.Imaging_kd_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_Hill_Toggle_layout.addWidget(self.ui.Imaging_Hill_toggleButton)
    self.ui.Imaging_Hill_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_PhotoShotNoise_Toggle_layout.addWidget(self.ui.Imaging_PhotoShotNoise_toggleButton)
    self.ui.Imaging_PhotoShotNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_FluoNoise_Toggle_layout.addWidget(self.ui.Imaging_FluoNoise_toggleButton)
    self.ui.Imaging_FluoNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_FluoScale_Toggle_layout.addWidget(self.ui.Imaging_FluoScale_toggleButton)
    self.ui.Imaging_FluoScale_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_FluoOffset_Toggle_layout.addWidget(self.ui.Imaging_FluoOffset_toggleButton)
    self.ui.Imaging_FluoOffset_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.Imaging_Saturation_Toggle_layout.addWidget(self.ui.Imaging_Saturation_toggleButton)
    self.ui.Imaging_Saturation_toggleButton.setChecked(True)
    Page201.Imaging201.ActivateFluoSat(self)
    self.ui.Imaging_Saturation_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    # Generate toggle buttons for Multiple Imaging Page
    self.ui.MultipleImaging_FrameRate_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                              circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                              active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                              )
    self.ui.MultipleImaging_PMT_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                        circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                        active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                        )
    self.ui.MultipleImaging_Laser_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                          circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                          active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                          )

    self.ui.MultipleImaging_CalciumDecay_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                                 circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                                 active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                                 )
    self.ui.MultipleImaging_CalciumJump_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                                circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                                active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                                )
    self.ui.MultipleImaging_CalciumNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                                 circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                                 active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                                 )
    self.ui.MultipleImaging_CalciumBaseline_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                                    circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                                    active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[10])
                                                                    )

    self.ui.MultipleImaging_kd_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                       circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                       active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                       )
    self.ui.MultipleImaging_Hill_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                         circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                         active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                         )
    self.ui.MultipleImaging_PhotoShotNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                                   circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                                   active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                                   )
    self.ui.MultipleImaging_FluoNoise_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                              circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                              active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                              )
    self.ui.MultipleImaging_FluoScale_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                              circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                              active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                              )
    self.ui.MultipleImaging_FluoOffset_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                               circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                               active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                               )
    self.ui.MultipleImaging_Saturation_toggleButton = PyToggle(bg_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[11]),
                                                               circle_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[15]),
                                                               active_color='#%02x%02x%02x' % tuple(Settings.DarkSolarized[4])
                                                               )

    self.ui.MultipleImaging_FrameRate_Toggle_layout.addWidget(self.ui.MultipleImaging_FrameRate_toggleButton)
    self.ui.MultipleImaging_FrameRate_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_PMT_Toggle_layout.addWidget(self.ui.MultipleImaging_PMT_toggleButton)
    self.ui.MultipleImaging_PMT_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_Laser_Toggle_layout.addWidget(self.ui.MultipleImaging_Laser_toggleButton)
    self.ui.MultipleImaging_Laser_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    self.ui.MultipleImaging_CalciumDecay_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumDecay_toggleButton)
    self.ui.MultipleImaging_CalciumDecay_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_CalciumJump_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumJump_toggleButton)
    self.ui.MultipleImaging_CalciumJump_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_CalciumNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_CalciumNoise_toggleButton)
    self.ui.MultipleImaging_CalciumNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_CalciumBaseline_Toggle_layout.addWidget(
        self.ui.MultipleImaging_CalciumBaseline_toggleButton)
    self.ui.MultipleImaging_CalciumBaseline_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

    self.ui.MultipleImaging_kd_Toggle_layout.addWidget(self.ui.MultipleImaging_kd_toggleButton)
    self.ui.MultipleImaging_kd_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_Hill_Toggle_layout.addWidget(self.ui.MultipleImaging_Hill_toggleButton)
    self.ui.MultipleImaging_Hill_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_PhotoShotNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_PhotoShotNoise_toggleButton)
    self.ui.MultipleImaging_PhotoShotNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_FluoNoise_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoNoise_toggleButton)
    self.ui.MultipleImaging_FluoNoise_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_FluoScale_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoScale_toggleButton)
    self.ui.MultipleImaging_FluoScale_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_FluoOffset_Toggle_layout.addWidget(self.ui.MultipleImaging_FluoOffset_toggleButton)
    self.ui.MultipleImaging_FluoOffset_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
    self.ui.MultipleImaging_Saturation_Toggle_layout.addWidget(self.ui.MultipleImaging_Saturation_toggleButton)
    self.ui.MultipleImaging_Saturation_toggleButton.setChecked(True)
    Page202.Imaging202.ActivateMultipleFluoSat(self)
    self.ui.MultipleImaging_Saturation_Toggle_layout.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
