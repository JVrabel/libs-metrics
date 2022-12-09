from SimulatedLIBS import simulation

def get_spectrum(return_wavelength=False, *args, **kwargs):
    spectrum = simulation.SimulatedLIBS(
        *args,
        **kwargs,
    ).get_interpolated_spectrum()
    if return_wavelength:
        return spectrum['intensity'].to_numpy(), spectrum['wavelength'].to_numpy()
    return spectrum['intensity'].to_numpy()