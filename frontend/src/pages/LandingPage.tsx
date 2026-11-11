import {
  ArrowRight,
  Bot,
  CandlestickChart,
  Check,
  Clock,
  FileBarChart,
  FileText,
  GitCompareArrows,
  Link2,
  ShieldCheck,
  Sparkles,
  Target,
  TriangleAlert,
} from 'lucide-react'
import type { CSSProperties } from 'react'
import { Link } from 'react-router-dom'
import { Logo } from '../components/ui/Logo'
import { Reveal } from '../components/ui/Reveal'
import { StatusChip } from '../components/ui/StatusChip'
import { trackPointer } from '../lib/pointer'

const features = [
  {
    icon: Bot,
    tone: 'primary',
    title: 'Conversational AI assistant',
    text: 'Ask about any stock in plain language and get structured answers with sources and assumptions.',
  },
  {
    icon: CandlestickChart,
    tone: 'govern',
    title: 'Technical analysis',
    text: 'Candlestick charts with volume, RSI, MACD and moving averages across timeframes.',
  },
  {
    icon: FileBarChart,
    tone: 'primary',
    title: 'Fundamental analysis',
    text: 'Income statement, balance sheet, cash flow, valuation metrics and earnings history.',
  },
  {
    icon: GitCompareArrows,
    tone: 'govern',
    title: 'Stock comparison',
    text: 'Put several companies side by side: prices, performance, metrics and indicators.',
  },
  {
    icon: Target,
    tone: 'primary',
    title: '5-year and 10-year goals',
    text: 'Set an investment goal and track your portfolio progress toward it.',
  },
  {
    icon: Sparkles,
    tone: 'caution',
    title: 'AI investment strategies',
    text: 'Explore long, short, diversification and balanced strategies with clearly labelled simulations.',
  },
] as const

const toneClasses = {
  primary: 'border-primary/30 bg-primary/10 text-primary-light',
  govern: 'border-govern/30 bg-govern/10 text-govern-soft',
  caution: 'border-caution/30 bg-caution/10 text-caution-light',
}

const steps = [
  { n: '01', title: 'Ask', text: 'Type a question about a stock, a comparison, your portfolio or a what-if scenario.' },
  { n: '02', title: 'Analyze', text: 'Market data and company research are analysed by the backend and the AI agent.' },
  { n: '03', title: 'Verify', text: 'Every answer shows where the data came from, when it is from and what was assumed.' },
]

const principles = [
  { icon: Link2, title: 'Data source', text: 'Shown with every financial result.' },
  { icon: Clock, title: 'Timestamp', text: 'Delayed data is never presented as real-time.' },
  { icon: FileText, title: 'Reporting period', text: 'Fundamentals state the period they cover.' },
  { icon: Check, title: 'Assumptions', text: 'Calculation assumptions stay visible.' },
  { icon: TriangleAlert, title: 'Simulation labels', text: 'Hypothetical results are never guaranteed returns.' },
]

const marquee = [
  'Technical analysis',
  'Fundamental analysis',
  'Stock comparison',
  'Portfolio analytics',
  'Risk breakdown',
  '5-year goals',
  '10-year goals',
  'Long / short simulations',
  'Sources & timestamps',
]

const delay = (ms: number) => ({ '--d': `${ms}ms` }) as CSSProperties

export function LandingPage() {
  return (
    <div className="min-h-screen overflow-x-hidden bg-canvas">
      {/* Top bar */}
      <header className="sticky top-0 z-30 border-b border-white/5 bg-canvas/75 backdrop-blur-md">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3.5 sm:px-6">
          <Logo className="text-lg" />
          <nav aria-label="Landing navigation" className="flex items-center gap-2">
            <span className="hidden sm:block">
              <Link to="/app/dashboard" className="btn btn-ghost">
                Dashboard
              </Link>
            </span>
            <Link to="/app/assistant" className="btn btn-primary">
              AI Assistant
            </Link>
          </nav>
        </div>
      </header>

      <main>
        {/* Hero */}
        <section className="relative">
          <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
            <div className="grid-bg absolute inset-0" />
            <div className="aurora -left-24 top-0 h-80 w-80 bg-primary" />
            <div className="aurora -right-24 top-24 h-96 w-96 bg-govern-alt" style={{ animationDelay: '-6s' }} />
          </div>

          <div className="relative mx-auto max-w-6xl px-4 pb-24 pt-20 text-center sm:px-6 sm:pt-28">
            <div className="enter" style={delay(0)}>
              <StatusChip tone="emerald" live>
                AI-powered stock market assistant
              </StatusChip>
            </div>
            <h1
              className="enter mx-auto mt-6 max-w-4xl text-4xl font-semibold leading-[1.08] tracking-tight text-ink sm:text-6xl"
              style={delay(100)}
            >
              Market data, research and analysis{' '}
              <span className="text-gradient">in one conversation</span>
            </h1>
            <p className="enter mx-auto mt-6 max-w-2xl text-base text-ink-soft sm:text-lg" style={delay(200)}>
              Financial Harness brings stock research, technical and fundamental analysis, portfolio tracking and AI-generated
              strategies together, so you can ask a question and see the evidence behind the answer.
            </p>
            <div className="enter mt-9 flex flex-wrap items-center justify-center gap-3" style={delay(300)}>
              <Link to="/app/assistant" className="btn btn-primary btn-lg">
                Ask the AI assistant <ArrowRight size={16} aria-hidden />
              </Link>
              <Link to="/app/dashboard" className="btn btn-secondary btn-lg">
                Open dashboard
              </Link>
            </div>

            {/* Anatomy of an answer: layout preview, no live data */}
            <div className="enter mx-auto mt-16 max-w-4xl text-left [perspective:1600px]" style={delay(450)}>
              <div className="panel-3d surface overflow-hidden !border-white/10 bg-panel/90 shadow-[0_40px_80px_-30px_rgba(0,0,0,0.8),0_0_0_1px_rgba(16,185,129,0.08)]">
                <div className="flex items-center gap-2 border-b border-white/5 px-4 py-3">
                  <span className="size-2.5 rounded-full bg-white/15" />
                  <span className="size-2.5 rounded-full bg-white/15" />
                  <span className="size-2.5 rounded-full bg-white/15" />
                  <span className="num ml-2 truncate text-xs text-ink-mute">financial-harness / anatomy of an answer</span>
                  <StatusChip tone="indigo" className="ml-auto shrink-0">
                    Layout preview · no live data
                  </StatusChip>
                </div>

                <div className="grid gap-6 p-5 sm:p-6 md:grid-cols-[1.35fr_1fr]">
                  <div>
                    <p className="num flex items-center gap-2 text-sm text-ink">
                      <span className="text-primary-light" aria-hidden>
                        &gt;
                      </span>
                      <span className="typing">Compare Apple and Microsoft.</span>
                    </p>

                    {/* Decorative chart. It has no values, axes or tickers. */}
                    <div className="relative mt-5 h-44 rounded border border-white/5 bg-canvas/70 p-3" aria-hidden>
                      <svg viewBox="0 0 400 140" className="size-full" preserveAspectRatio="none">
                        <defs>
                          <linearGradient id="area" x1="0" x2="0" y1="0" y2="1">
                            <stop offset="0" stopColor="#10b981" stopOpacity="0.35" />
                            <stop offset="1" stopColor="#10b981" stopOpacity="0" />
                          </linearGradient>
                        </defs>
                        {[28, 56, 84, 112].map((y) => (
                          <line key={y} x1="0" x2="400" y1={y} y2={y} stroke="rgba(255,255,255,0.05)" />
                        ))}
                        <path
                          className="fade-late"
                          d="M0 104 C40 98 60 76 100 82 S160 40 200 52 S270 90 310 58 S370 24 400 30 V140 H0 Z"
                          fill="url(#area)"
                        />
                        <path
                          className="draw"
                          pathLength={1000}
                          d="M0 104 C40 98 60 76 100 82 S160 40 200 52 S270 90 310 58 S370 24 400 30"
                          fill="none"
                          stroke="#34d399"
                          strokeWidth="2.5"
                          strokeLinecap="round"
                        />
                        <path
                          className="draw"
                          pathLength={1000}
                          style={{ animationDelay: '1s' }}
                          d="M0 92 C50 96 70 104 110 94 S170 70 210 78 S280 60 320 70 S380 56 400 62"
                          fill="none"
                          stroke="#60a5fa"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeDasharray="1000"
                        />
                      </svg>
                      <div className="absolute inset-x-3 bottom-3 flex h-8 items-end gap-1.5">
                        {[40, 65, 35, 80, 55, 70, 45, 90, 60, 50, 75, 42].map((h, i) => (
                          <span
                            key={i}
                            className="bar-rise flex-1 rounded-sm bg-govern/30"
                            style={{ height: `${h}%`, '--d': `${1200 + i * 60}ms` } as CSSProperties}
                          />
                        ))}
                      </div>
                    </div>
                  </div>

                  <ul className="space-y-3">
                    {[
                      { icon: Link2, label: 'Source' },
                      { icon: Clock, label: 'Timestamp' },
                      { icon: FileText, label: 'Reporting period' },
                      { icon: Check, label: 'Assumptions' },
                      { icon: TriangleAlert, label: 'Simulation label' },
                    ].map(({ icon: Icon, label }, i) => (
                      <li
                        key={label}
                        className="enter flex items-center gap-3 rounded border border-white/5 bg-canvas/60 px-3 py-2.5"
                        style={delay(1400 + i * 120)}
                      >
                        <span className="grid size-7 place-items-center rounded border border-primary/25 bg-primary/10 text-primary-light">
                          <Icon size={14} aria-hidden />
                        </span>
                        <span className="min-w-0 flex-1">
                          <span className="num block text-[10px] uppercase tracking-wider text-ink-mute">{label}</span>
                          <span className="skeleton mt-1.5 block h-2 w-3/4" aria-hidden />
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Capability marquee */}
        <section aria-label="Capabilities" className="marquee overflow-hidden border-y border-white/5 bg-deep/60 py-4">
          <div className="marquee-track">
            {[0, 1].map((copy) => (
              <ul key={copy} className="flex shrink-0 items-center" aria-hidden={copy === 1}>
                {marquee.map((item) => (
                  <li key={item} className="num flex items-center text-xs uppercase tracking-[0.2em] text-ink-soft">
                    <span className="px-8">{item}</span>
                    <span className="size-1 rounded-full bg-primary/70" aria-hidden />
                  </li>
                ))}
              </ul>
            ))}
          </div>
        </section>

        {/* Features */}
        <section aria-labelledby="features-heading" className="mx-auto max-w-6xl px-4 py-24 sm:px-6">
          <Reveal className="mx-auto mb-12 max-w-2xl text-center">
            <p className="num mb-3 text-xs uppercase tracking-[0.2em] text-primary-light">Capabilities</p>
            <h2 id="features-heading" className="text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
              Everything an investor needs, in one workspace
            </h2>
          </Reveal>
          <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
            {features.map(({ icon: Icon, tone, title, text }, i) => (
              <li key={title}>
                <Reveal delay={(i % 3) * 90} className="h-full">
                  <div onMouseMove={trackPointer} className="surface spotlight lift h-full p-6">
                    <span className={`mb-4 grid size-11 place-items-center rounded border ${toneClasses[tone]}`} aria-hidden>
                      <Icon size={20} />
                    </span>
                    <h3 className="text-lg font-medium tracking-tight text-ink">{title}</h3>
                    <p className="mt-1.5 text-sm leading-relaxed text-ink-soft">{text}</p>
                  </div>
                </Reveal>
              </li>
            ))}
          </ul>
        </section>

        {/* How it works */}
        <section aria-labelledby="how-heading" className="border-y border-white/5 bg-deep/50 py-24">
          <div className="mx-auto max-w-6xl px-4 sm:px-6">
            <Reveal className="mx-auto mb-14 max-w-2xl text-center">
              <p className="num mb-3 text-xs uppercase tracking-[0.2em] text-primary-light">How it works</p>
              <h2 id="how-heading" className="text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
                From question to evidence in three steps
              </h2>
            </Reveal>
            <ol className="relative grid gap-6 md:grid-cols-3">
              <div aria-hidden className="flow-line absolute left-[16%] right-[16%] top-7 hidden h-px md:block" />
              {steps.map((s, i) => (
                <li key={s.n}>
                  <Reveal delay={i * 140}>
                    <div className="text-center">
                      <span className="num relative mx-auto grid size-14 place-items-center rounded-full border border-primary/40 bg-canvas text-lg text-primary-light shadow-[0_0_28px_-6px_rgba(16,185,129,0.7)]">
                        {s.n}
                      </span>
                      <h3 className="mt-5 text-xl font-medium text-ink">{s.title}</h3>
                      <p className="mx-auto mt-2 max-w-xs text-sm leading-relaxed text-ink-soft">{s.text}</p>
                    </div>
                  </Reveal>
                </li>
              ))}
            </ol>
          </div>
        </section>

        {/* Transparency */}
        <section aria-labelledby="trust-heading" className="mx-auto max-w-6xl px-4 py-24 sm:px-6">
          <div className="grid items-center gap-12 lg:grid-cols-[1fr_1.1fr]">
            <Reveal>
              <p className="num mb-3 flex items-center gap-2 text-xs uppercase tracking-[0.2em] text-primary-light">
                <ShieldCheck size={14} aria-hidden /> Built on transparency
              </p>
              <h2 id="trust-heading" className="text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
                You always see where a number came from
              </h2>
              <p className="mt-4 text-ink-soft">
                Financial Harness never hides its evidence. Charts and tables come from backend data, and the app does not invent prices,
                indicators or AI answers.
              </p>
            </Reveal>
            <ul className="space-y-3">
              {principles.map(({ icon: Icon, title, text }, i) => (
                <li key={title}>
                  <Reveal delay={i * 80}>
                    <div
                      onMouseMove={trackPointer}
                      className="surface spotlight lift flex items-center gap-4 px-4 py-3.5"
                    >
                      <span className="grid size-9 shrink-0 place-items-center rounded border border-primary/25 bg-primary/10 text-primary-light" aria-hidden>
                        <Icon size={16} />
                      </span>
                      <div>
                        <p className="text-sm font-medium text-ink">{title}</p>
                        <p className="text-sm text-ink-soft">{text}</p>
                      </div>
                    </div>
                  </Reveal>
                </li>
              ))}
            </ul>
          </div>
        </section>

        {/* Call to action */}
        <section className="px-4 pb-24 sm:px-6">
          <Reveal>
            <div className="surface relative mx-auto max-w-4xl overflow-hidden px-6 py-14 text-center">
              <div aria-hidden className="aurora left-1/2 top-0 h-56 w-56 -translate-x-1/2 bg-primary opacity-25" />
              <h2 className="relative text-3xl font-semibold tracking-tight text-ink sm:text-4xl">Start with a question</h2>
              <p className="relative mx-auto mt-3 max-w-xl text-ink-soft">
                Open the assistant or explore the dashboard. Everything you see is labelled with its source.
              </p>
              <div className="relative mt-8 flex flex-wrap justify-center gap-3">
                <Link to="/app/assistant" className="btn btn-primary btn-lg">
                  Ask the AI assistant <ArrowRight size={16} aria-hidden />
                </Link>
                <Link to="/app/dashboard" className="btn btn-secondary btn-lg">
                  Open dashboard
                </Link>
              </div>
            </div>
          </Reveal>
        </section>
      </main>

      <footer className="border-t border-white/5 px-4 py-8 text-center text-xs text-ink-mute">
        <Logo className="mb-3 text-sm" />
        <p>Financial Harness provides analysis for information only. It is not financial advice.</p>
      </footer>
    </div>
  )
}
