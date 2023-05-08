import { useState } from 'react';
import { Html } from '@react-three/drei';
import { useNavigate } from 'react-router-dom';

const App = () => {
	const navigator = useNavigate();

	const [showSkullList, setSkullList] = useState<boolean>(false);
	const [showSphereList, setSphereList] = useState<boolean>(false);

	return (
		<Html
			className="w-screen min-h-screen flex flex-col content-center"
			style={{ width: 200 }}
			center
		>
			<div className="m-auto flex flex-col">
				<div className="mt-2 mb-2 p-2 text-center bg-gray-500 border-2 rounded-md hover:cursor-pointer">
					<h1 onClick={() => setSkullList((val) => (val = !val))}>
						Skull Dataset
					</h1>
					{showSkullList && (
						<ul className="bg-gray-200 text-black">
							<li>
								<a onClick={() => navigator('/skull/PolyCam')}>
									PolyCam
								</a>
							</li>
							<li>
								<a onClick={() => navigator('/skull/Kinect')}>
									Kinect
								</a>
							</li>
							<li>
								<a onClick={() => navigator('/skull/Point_E')}>
									Point-E
								</a>
							</li>
						</ul>
					)}
				</div>
				<div className="mt-2 mb-2 p-2 text-center bg-gray-500 border-2 rounded-1">
					<h1
						className="hover:cursor-pointer hover:bg-gray-700 hover:text-gray"
						onClick={() => setSphereList((val) => (val = !val))}
					>
						Sphere Dataset
					</h1>
					{showSphereList && (
						<ul className="bg-gray-200 text-black">
							<li>
								<a onClick={() => navigator('/sphere/PolyCam')}>
									PolyCam
								</a>
							</li>
							<li>
								<a onClick={() => navigator('/sphere/Kinect')}>
									Kinect
								</a>
							</li>
							<li>
								<a onClick={() => navigator('/sphere/Point_E')}>
									Point-E
								</a>
							</li>
						</ul>
					)}
				</div>
			</div>
		</Html>
	);
};

export default App;
