import Root from '@/components/tunnels/Root';
import { Html } from '@react-three/drei';
import { useNavigate } from 'react-router-dom';

const App = () => {
	const navigator = useNavigate();

	return (
		<Root.In>
			<main className="absolute z-10 h-screen w-screen flex flex-col items-center justify-center gap-3">
				<div className="flex flex-col justify-center items-center gap-3">
					<button
						className="px-4 py-2 bg-primary border-2 border-accent rounded-md hover:bg-secondary hover:text-highlight"
						onClick={() => navigator('/method')}
					>
						Method
					</button>
					<button
						className="px-4 py-2 bg-primary border-2 border-accent rounded-md hover:bg-secondary hover:text-highlight"
						onClick={() => navigator('/dataset')}
					>
						Dataset
					</button>
				</div>
			</main>
		</Root.In>
	);
};

export default App;
