import collections

class StdStationPlot(self):

    def __init__(self):
        # define where the obs go on the station plot model
        # value must be on the grid:
        # x : [-2, 2]
        # y : [-3, 2]
        self._totalCloudCoverMapper = GroupSymbolMapper(tcc_start)

        self.stationPlotModelPosition = collections.namedtuple('x', 'y')

        self.total_cloud_cover_spmp = StationPlotModelPosition(0, 0)

    def add_value(x, y, pos, vals):
        pos_nt = StationPlotModelPosition(pos[0], pos[1])
        station_plot(x, y, pos_nt, vals)

    def add_total_cloud_cover(self, vals):
        ```
        ```
        x = self.total_cloud_cover_spmp.x
        y = self.total_cloud_cover_spmp.y

        station_plot(x, y, pos, val)

class SymbolMapper():
    def __init__(self)
        # dict of wmo code to font code point
        self.full_map = {}

    def lookup_by_wmo_code(wmo_code):

        return self.full_map(wmo_code)

class GroupSymbolMapper():
    def __init__(self, first_code_point)
        self.start = first_code_point

    def lookup_by_val(i):
        return self.start + i



def station_plot(x, y, pos, vals):

    return None
