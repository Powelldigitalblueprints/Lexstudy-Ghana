function App() {
  return (
    <main className="page-shell">
      <header className="topbar">
        <a className="wordmark" href="/" aria-label="Legum home">LEGUM</a>
        <span className="topbar-note">Legal studies and research</span>
      </header>
      <section className="welcome-panel">
        <p className="eyebrow">A learning space for law</p>
        <h1>Study the law with clarity.</h1>
        <p className="intro">
          Your academic workspace for course materials, Ghanaian legal
          authorities, case briefs and structured practice.
        </p>
        <div className="status-line"><span className="status-dot" />Development environment is ready</div>
      </section>
      <section className="feature-grid" aria-label="Platform areas">
        <article className="feature-card"><span className="card-number">01</span><h2>Course notes</h2><p>Organised materials for core law subjects and topics.</p></article>
        <article className="feature-card"><span className="card-number">02</span><h2>Case briefs</h2><p>Structured summaries with citations and source details.</p></article>
        <article className="feature-card"><span className="card-number">03</span><h2>Learning tools</h2><p>Quizzes, flashcards, IRAC exercises and mock assessments.</p></article>
      </section>
      <footer className="footer"><span>Legum</span><span>Independent legal studies platform</span></footer>
    </main>
  );
}

export default App;
