import { useNavigate } from 'react-router-dom';
import Root from '@/components/tunnels/Root';

const DatasetHome = () => {
	const navigator = useNavigate();

	return (
		<Root.In>
			<main className="absolute z-10 h-screen w-screen flex flex-col items-center justify-center gap-3">
				<div className="m-auto flex flex-row gap-4 bg-tertiary rounded-md border-2 border-accent p-4">
					<div className="p-2 text-center bg-secondary">
						<button className="text-highlight rounded-md">
							Skull Dataset
						</button>

						<ul className="flex flex-col bg-gray-200 text-accent bg-tertiary">
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('Skull/PolyCam')}
								>
									PolyCam
								</button>
							</li>
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('Skull/Kinect')}
								>
									Kinect
								</button>
							</li>
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('Skull/Point_E')}
								>
									Point-E
								</button>
							</li>
						</ul>
					</div>
					<div className="p-2 text-center bg-secondary">
						<button className="text-highlight">
							Sphere Dataset
						</button>
						<ul className="flex flex-col bg-gray-200 text-accent bg-tertiary">
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('Sphere/PolyCam')}
								>
									PolyCam
								</button>
							</li>
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('Sphere/Kinect')}
								>
									Kinect
								</button>
							</li>
							<li>
								<button
									className="grid place-content-center w-full h-full p-2 hover:bg-highlight hover:text-secondary rounded-md"
									onClick={() => navigator('sphere/Point_E')}
								>
									Point-E
								</button>
							</li>
						</ul>
					</div>
				</div>
				<a
					className="m-5 bg-tertiary text-accent p-2 hover:cursor-pointer hover:bg-highlight rounded-md hover:text-secondary"
					onClick={() => navigator('/')}
				>
					Return
				</a>
			</main>
		</Root.In>
	);
};

export default DatasetHome;
