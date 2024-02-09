const app = document.getElementById('app');

function Header({title}) {
    // console.log(title)
    // {} means *javascript land*
    return(<h1>My name is {title}</h1>);
    // return(<h1>{`My name is ${title}`}</h1>);
    // return(<h1>{title ? title : 'Default title'}</h1>);
}

function HomePage() {
    // set default as 0
    const [likesCount, setLikesCount] = React.useState(0);

    function handleLikeClick() {
        // console.log('increment like count');
        setLikesCount(likesCount + 1);
    }

    const names = ['Ada Lovelace', 'Grace Hopper', 'Margaret Hamilton'];

    return <div>
        <Header title='react' />
        <Header title='not svelte' />

        <ul>
            {
                names.map(name => (
                    <li key={name}>{name}</li>
                ))
            }
        </ul>

        <button onClick={handleLikeClick}>Like({likesCount})</button>
    </div>
}

const root = ReactDOM.createRoot(app);
root.render(<HomePage />);