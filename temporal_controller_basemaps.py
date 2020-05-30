# Using #raster layers on QGIS Temporal Controller

# Set deactivate controller
for i, layer in enumerate(QgsProject.instance().mapLayers().values()):
    propeties = layer.temporalProperties()
    propeties.setIsActive(False)

# Set temporal properties
for i, layer in enumerate(QgsProject.instance().mapLayers().values()):
    if isinstance(layer, QgsRasterLayer):
        mode = QgsRasterLayerTemporalProperties.ModeFixedTemporalRange
        propeties = layer.temporalProperties()
        propeties.setFixedTemporalRange(QgsDateTimeRange(QDateTime(QDate(2020, 1, 1), QTime(1, i, 0, 0), Qt.UTC),
                                                         QDateTime(QDate(2020, 1, 1), QTime(1, 1 + i, 0, 0), Qt.UTC)))
        propeties.setMode(mode)
        propeties.setIsActive(True)
