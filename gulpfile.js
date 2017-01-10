var gulp = require('gulp'),
    usemin = require('gulp-usemin'),
    del = require('del'),
    runSequence = require('run-sequence'),
    cssmin = require('gulp-css'),
    rev = require('gulp-rev'),
    rename = require('gulp-rename'),
    shell = require('gulp-shell'),
    argv = require('yargs').argv;;

gulp.task("build:clean", function () {
    return del(["build"]);
})

gulp.task("build:dependencies", function () {
    return gulp.src(["requirements.txt"])
        .pipe(gulp.dest("build"))
})

gulp.task("build:backend", function () {
    return gulp.src(["**/*.py", "**/*.cfg", "!virtualenv/**/*"])
        .pipe(gulp.dest("build"))
})

gulp.task("build:frontend", function () {
    return gulp.src('**/templates/**/*.html')
        .pipe(usemin({
            assetsDir: "./app",
            path: ".",
            css: [rev(), rename({ dirname: 'app/static' })],
            js: [rev(), rename({ dirname: 'app/static' })]
        }))
        .pipe(gulp.dest('build'));
})

gulp.task("build", function (cb) {
    return runSequence("build:clean", ["build:backend", "build:dependencies", "build:frontend"], cb)
})

gulp.task("deploy", function (cb) {
    return runSequence("build", "push", cb)
})

gulp.task("push", shell.task([
    'echo hello' + argv["app"]
]));

